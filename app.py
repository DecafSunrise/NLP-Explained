import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    Sentiment_Analysis,
    Keyword_Extraction,
    Text_Summarization)
# st.set_page_config()
st.set_page_config(page_title="NLP for Me", page_icon="📜", layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Home", home.app)
apps.add_app("Sentiment Analysis", Sentiment_Analysis.app)
apps.add_app("Keyword Extraction", Keyword_Extraction.app)
apps.add_app("Text Summarization", Text_Summarization.app)

# The main app
apps.run()