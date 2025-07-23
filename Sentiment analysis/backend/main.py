from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("D:\My project\Sentiment analysis\model\sentiment_model.pkl")

app = FastAPI()

# Request body model
class InputText(BaseModel):
    text: str

# Test endpoint
@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running."}

# Prediction endpoint
@app.post("/predict/")
def predict_sentiment(data: InputText):
    prediction = model.predict([data.text])[0]  # Get 0 or 1
    sentiment = "positive" if prediction == 1 else "negative"
    return {
        "sentiment": sentiment
    }