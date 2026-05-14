import streamlit as st
import asyncio
import websockets
import json
import pandas as pd

st.title("🚨 REAL-TIME IoT DASHBOARD")

data_buffer = []

async def listen():
    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as websocket:

        await websocket.send("connect")

        while True:
            msg = await websocket.recv()
            data = json.loads(msg)

            data_buffer.append(data)

            df = pd.DataFrame(data_buffer)

            st.write(df)
            st.line_chart(df[["temperature", "vibration"]])

asyncio.run(listen())