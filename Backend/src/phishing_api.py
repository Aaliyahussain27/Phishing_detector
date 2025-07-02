from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
from .THE_CODE import extract_features

app = FastAPI()

# Enable CORS so Android app can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 For now, open to all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
model = joblib.load("phishing_model.pkl")

# Request format validation (Pydantic)
class UrlRequest(BaseModel):
    url: str

@app.post("/predict")
def predict(data: UrlRequest):
    url = data.url
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided")

    features = extract_features(url)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]

    result = "Phishing" if prediction == 1 else "Legit"
    return {"result": result}

@app.get("/")
def root():
    return {"message": "FastAPI Phishing Detector is Live 💥"}
