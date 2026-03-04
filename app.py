from fastapi import FastAPI
import joblib
import json
import pandas as pd
import os

app = FastAPI(title="Fraud Detection API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "lgbm_champion.pkl")
threshold_path = os.path.join(BASE_DIR, "models", "lgbm_threshold.json")

model = joblib.load(model_path)

with open(threshold_path, "r") as f:
    threshold_data = json.load(f)

threshold = threshold_data["threshold"]

@app.post("/score")
def score_transaction(features: dict):
    df = pd.DataFrame([features])
    prob = model.predict_proba(df)[0][1]
    decision = "FLAG" if prob >= threshold else "APPROVE"
    return {
        "fraud_probability": float(prob),
        "decision": decision
    }
