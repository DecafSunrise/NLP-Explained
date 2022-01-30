import streamlit as st
import webbrowser
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from textblob import TextBlob
# https://lmgtfy.app/?q=sentiment+analysis
def app():
    title = st.title("Sentiment Analysis")
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6, row1_col7, row1_col8 = st.columns(8)

    with row1_col1:
        if st.button('Wikipedia Page'):
            webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Sentiment_analysis')

    with row1_col2:
        if st.button("Google it"):
            webbrowser.open_new_tab("https://www.google.com/search?q=sentiment+analysis")


     # st.text(title.replace(' ', '+'))
    # st.title
    with st.expander("See Explanation"):
        st.markdown("""
        ### Description of the Task:
        *Sentiment analysis* (also known as *opinion mining* or *emotion AI*) is the use of natural language 
        processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, 
        and study affective states and subjective information. Commonly, this takes the form of Sentiment analysis is widely
         applied to voice of the customer materials such as reviews and survey responses, online and social media, and 
         healthcare materials for applications that range from marketing to customer service to clinical medicine.  
           
         ### Description of the Output:  
         Sentiment Analysis packages will output a score from -1 to 1. Text with lots of negative words will be closer to -1,
          while positive text will be closer to +1. Neutral text would be 0. Often, python packages will split these scores
           into several sub-scores: *Polarity* and *Subjectivity* are common components.
         """)

    # st.text("")
    text = st.text_area("Put some text in the box below, to give Sentiment Analysis a test drive!")
    Analyzer = st.radio(
        "Select a python package to perform the analysis",
        ('TextBlob', 'VADER'))
    if st.button("Run"):
        if Analyzer=="TextBlob":
            blob = TextBlob(text)
            for sentence in blob.sentences:
                st.text(sentence)
                st.text(f"\t{sentence.sentiment}")
        if Analyzer=="VADER" and (len(text)>0):
            # st.text(f"{len(text)}")
            sentences  = re.split(r' *[\.\?!][\'"\)\]]* *', text)
            VaderAnalyzer = SentimentIntensityAnalyzer()
            for sentence in sentences:
                st.text(sentence)
                st.text(VaderAnalyzer.polarity_scores(sentence))
                # vs =
                # print("{:-<65} {}".format(sentence, str(vs)))

if __name__ == "__main__":
    app()