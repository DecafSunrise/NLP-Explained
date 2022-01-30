import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    Sentiment_Analysis,)
# st.set_page_config()
st.set_page_config(page_title="NLP for Me", page_icon="📜", layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Home", home.app)
apps.add_app("Sentiment Analysis", Sentiment_Analysis.app)
# apps.add_app("Plot a CSV on the map", Map_Plotter.app)
# apps.add_app("Monitor OLS News", OLS_Monitor.app)
# apps.add_app("Network Explorer", Network_Explorer.app)


# The main app
apps.run()