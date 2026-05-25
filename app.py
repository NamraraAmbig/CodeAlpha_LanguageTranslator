import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")

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
    translated = GoogleTranslator(
        source='auto',
        target=languages[language]
    ).translate(text)

    st.success(translated)
