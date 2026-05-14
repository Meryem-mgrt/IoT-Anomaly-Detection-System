# ENTRY POINT (FastAPI server)
from fastapi import FastAPI, WebSocket, Depends
from database.db import save_data, get_data
from backend.auth import verify_token

app = FastAPI()

# -------------------------
# ACTIVE WEBSOCKET CLIENTS
# -------------------------
clients = []

# -------------------------
# MQTT / DEVICE DATA ENTRY
# -------------------------
@app.post("/data")
def receive_data(data: dict, user=Depends(verify_token)):

    if user["role"] not in ["device", "admin"]:
        return {"error": "forbidden"}

    save_data(data)

    # 🔥 PUSH TO ALL CLIENTS (REAL TIME)
    for c in clients:
        import asyncio
        asyncio.create_task(c.send_json(data))

    return {"status": "saved"}

# -------------------------
# STREAMING ENDPOINT
# -------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)