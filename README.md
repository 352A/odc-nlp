# Sentiment Analysis App Using Machine Learning

This project is a **Sentiment Analysis App** built using **Streamlit** and **scikit-learn**. It allows users to input a review and get a sentiment prediction (e.g., positive or negative) based on a pre-trained machine learning model.

## Features

- **Interactive Web Interface**: Built using Streamlit for ease of use.
- **Machine Learning Powered**: Utilizes a trained model to predict sentiment.
- **Preprocessing Pipeline**: Implements text preprocessing with tokenization, stopword removal, and stemming.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/352A/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data**

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```
