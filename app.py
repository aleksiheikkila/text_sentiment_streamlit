import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.write("# Real Time Text Sentiment Analysis")

user_input = st.text_input("Please give your feedback: ")
nltk.download("vader_lexicon")

s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Sentiment: Negative")
elif score["pos"] != 0:
    st.write("# Sentiment: Positive")
