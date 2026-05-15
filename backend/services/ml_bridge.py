import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "ml_service" / "model" / "modele_isolation_forest.pkl"

model = joblib.load(MODEL_PATH)


def run_prediction(data: dict):

    features = [[
        data.get("temperature", 0),
        data.get("vibration", 0),
        data.get("pressure", 0),
        data.get("speed", 0)
    ]]

    prediction = model.predict(features)[0]

    return {
        "machine_id": data.get("machine_id"),
        "anomaly": int(prediction),
        "raw_input": data
    }