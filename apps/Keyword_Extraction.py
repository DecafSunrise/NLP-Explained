import streamlit as st
import webbrowser
import re
import yake

from textblob import TextBlob


# https://lmgtfy.app/?q=sentiment+analysis
def app():
    title = st.title("Keyword Extraction")
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6, row1_col7, row1_col8 = st.columns(8)

    with row1_col1:
        if st.button('Wikipedia Page'):
            webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Keyword_extraction')

    with row1_col2:
        if st.button("Google it"):
            webbrowser.open_new_tab("https://www.google.com/search?q=RAKE+Keyword+extraction")

    # st.text(title.replace(' ', '+'))
    # st.title
    with st.expander("See Explanation"):
        st.markdown("""
        ### Description of the Task:
        **Keyword extraction** is tasked with the automatic identification of terms that best describe the subject of a document. RAKE (Rapid Automatic Keyword Extraction) is one of the most famous algorithms.
    
        ### Description of the Output:  
        The output of RAKE or YAKE keyword extraction will be a list of keywords, and associated scores. Depending on the algorithm these scores can be on a 0-1 scale, or an arbitrary scale above 1.
         """)

    # st.text("")
    text = st.text_area("Put some text in the box below, to give Keyword Extraction a test drive!")
    # Analyzer = st.radio(
    #     "Select a python package to perform the analysis",
    #     ('TextBlob', 'VADER'))
    if st.button("Run"):
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(text)
        # st.text(keywords)
        for kw in keywords:
            st.text(kw)


if __name__ == "__main__":
    app()