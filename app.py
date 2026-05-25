import streamlit as st
from googletrans import Translator

st.title("Language Translator")

translator = Translator()

text = st.text_area("Enter text")

languages = {
    "Hindi": "hi",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

language = st.selectbox("Select Language", list(languages.keys()))

if st.button("Translate"):
    translated = translator.translate(text, dest=languages[language])
    st.success(translated.text)
