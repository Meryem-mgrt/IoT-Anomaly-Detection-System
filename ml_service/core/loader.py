import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "modele_isolation_forest.pkl"

model = joblib.load(MODEL_PATH)