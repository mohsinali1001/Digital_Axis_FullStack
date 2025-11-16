from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
from pathlib import Path

app = FastAPI(title="DigitalAxis ML Model Service")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
MODEL_PATH = Path(__file__).parent / "model" / "pipe.pkl"
model = None

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print(f"✅ Model loaded from {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print(f"Model path: {MODEL_PATH}")
    print(f"Current directory: {os.getcwd()}")


class IncomingData(BaseModel):
    network_packet_size: float
    protocol_type: str
    login_attempts: int
    session_duration: float
    encryption_used: str
    ip_reputation_score: float
    failed_logins: int
    browser_type: str
    unusual_time_access: int


@app.get("/")
def root():
    return {"message": "DigitalAxis ML Model Service", "model_loaded": model is not None}


@app.post("/predict")
def predict(data: IncomingData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        # Convert input to model format
        # Adjust based on your actual model's expected input format
        features = [
            data.network_packet_size,
            data.protocol_type,
            data.login_attempts,
            data.session_duration,
            data.encryption_used,
            data.ip_reputation_score,
            data.failed_logins,
            data.browser_type,
            data.unusual_time_access,
        ]

        # If your model expects a different format, adjust here
        # For example, if it needs encoding for categorical features:
        # You might need to use LabelEncoder or OneHotEncoder
        
        # Simple prediction (adjust based on your model)
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0] if hasattr(model, "predict_proba") else [0.5, 0.5]
        
        # Determine if attack detected (1 = attack, 0 = normal)
        attack_detected = bool(prediction == 1)
        attack_probability = float(probability[1] if len(probability) > 1 else probability[0])

        return {
            "prediction": int(prediction),
            "probability": attack_probability,
            "attack_detected": attack_detected,
            "locked_state": attack_detected,  # Lock if attack detected
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }

