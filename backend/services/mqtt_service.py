# MQTT consumer

import json
import paho.mqtt.client as mqtt

from backend.database.db import SessionLocal
from backend.database.models import SensorData
from backend.services.stream import manager

MQTT_BROKER = "mqtt-broker"
MQTT_PORT = 1883
TOPIC = "factory/sensors"

# -------------------------
# DB SAVE FUNCTION
# -------------------------
def save_to_db(data):
    db = SessionLocal()

    try:
        record = SensorData(
            machine_id=data["machine_id"],
            temperature=data["temperature"],
            vibration=data["vibration"]
        )

        db.add(record)
        db.commit()
        db.refresh(record)

    finally:
        db.close()

# -------------------------
# MQTT CALLBACK
# -------------------------
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())

        print("📡 MQTT RECEIVED:", payload)

        # 1. Save to DB
        save_to_db(payload)

        # 2. Broadcast to dashboard
        import asyncio
        asyncio.create_task(manager.broadcast(payload))

        # 3. (HOOK) ML prediction later
        # predict(payload)

    except Exception as e:
        print("❌ MQTT error:", e)

# -------------------------
# MQTT SETUP
# -------------------------
client = mqtt.Client()
client.on_message = on_message

def start_mqtt():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.subscribe(TOPIC)
    client.loop_start()