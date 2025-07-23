# frontend/app.py
import streamlit as st
import requests

st.title("🎬 Sentiment Analysis on Movie Reviews")
st.write("Enter a review and see if it's Positive or Negative!")

# Text input
user_input = st.text_area("📝 Type your movie review here")

# Button
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Send request to FastAPI
        response = requests.post("http://127.0.0.1:8000/predict/", json={"text": user_input})
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Sentiment: **{result['sentiment'].capitalize()}**")
        else:
            st.error("Something went wrong with the API.")
