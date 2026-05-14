import paho.mqtt.client as mqtt
import json
import requests

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    print("MQTT:", data)

    # send to backend
    requests.post(
        "http://localhost:8000/data",
        json=data,
        headers={"x-token": "DEVICE_TOKEN"}
    )

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("iot/device/data")

client.loop_forever()