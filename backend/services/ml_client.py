# calls ML service

import requests

ML_URL = "http://ml_service:9000/predict"

def get_prediction(payload):
    res = requests.post(ML_URL, json=payload)
    return res.json()