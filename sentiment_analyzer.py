import streamlit as st
from fastai.text.all import load_learner

st.set_page_config(layout="wide")

classifier = load_learner("./models/trained.pkl")

st.title("IIITN चलचित्र समीक्षा भावना विश्लेषक में आपका स्वागत है🙏")
review = st.text_area(label="फिल्म समीक्षा दर्ज करें(Enter movie review)", placeholder="टाइपिंग शुरू करने के लिए क्लिक करें...", height=400)
button = st.button("भाव अनुमानित करे")

preds_hindi = ["नकारात्मक 😔", "तटस्थ 😑", "सकारात्मक 😄"]
preds_english = ["Negative 😔", "Neutral 😑", "Positive 😄"]

if button:
  if len(review) >= 100:
    prediciton = classifier.predict(review)
    sentiment_index = int(prediciton[0])
    st.code(f"अनुमानित भावना: {preds_hindi[sentiment_index]}")
    st.code(f"Predicted Sentiment: {preds_english[sentiment_index]}")
    