from ml_service.core.loader import model


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