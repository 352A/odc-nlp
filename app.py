import streamlit as st
import sklearn
import helper
import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

st.title("Sentiment Analysis App Using ML")
st.markdown("""
This app predicts the sentiment (Positive or Negative) of the sentence you enter.
""")

text = st.text_input("Enter a sentence for sentiment analysis:")

if st.button("Predict"):
    if not text.strip():
        st.error("Please enter valid text to analyze.")
    else:
        token = helper.preprocessing_step(text)
        vectorized_data = vectorizer.transform([token])
        prediction = model.predict(vectorized_data)
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.success(f"The sentiment is **{sentiment}**.")  