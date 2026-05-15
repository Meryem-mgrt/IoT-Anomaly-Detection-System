from fastapi import FastAPI, WebSocket
from sqlalchemy.orm import Session

from backend.database.db import engine, SessionLocal
from backend.database.base import Base
from backend.database.models import SensorData

from backend.api.auth import router as auth_router

from backend.services.mqtt_service import start_mqtt
from backend.services.stream import manager

from backend.services.ml_client import get_prediction
from backend.services.alert_service import send_alert

app = FastAPI(title="PFA Industrial Monitoring API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include auth routes
app.include_router(auth_router)

# Start MQTT listener
start_mqtt()


@app.get("/")
def home():
    return {"status": "running"}


# -----------------------------
# WEBSOCKET
# -----------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except:
        manager.disconnect(websocket)


# -----------------------------
# SENSOR DATA API
# -----------------------------
@app.post("/data")
async def receive_data(data: dict):

    db: Session = SessionLocal()

    try:
        # Save sensor data
        sensor = SensorData(
            machine_id=data["machine_id"],
            temperature=data["temperature"],
            vibration=data["vibration"]
        )

        db.add(sensor)
        db.commit()

        # ML prediction
        result = get_prediction(data)

        print("🧠 Prediction:", result)

        # Alert if anomaly
        if result["anomaly"] == 1:

            send_alert(
                message=f"⚠️ Anomaly detected on machine {result['machine_id']}",
                severity="high"
            )

        # Broadcast realtime
        await manager.broadcast({
            "sensor": data,
            "prediction": result
        })

        return {
            "status": "success",
            "prediction": result
        }

    finally:
        db.close()