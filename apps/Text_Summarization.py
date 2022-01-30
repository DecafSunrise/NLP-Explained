import streamlit as st
import webbrowser
import re
import nltk
import heapq


def summarize(k, text):
    # Removing Square Brackets and Extra Spaces
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Removing special characters and digits
    formatted_text = re.sub('[^a-zA-Z]', ' ', text)
    formatted_text = re.sub(r'\s+', ' ', formatted_text)

    #     formatted_article_text = article_text.replace("\t", ' ', formatted_article_text)

    sentence_list = nltk.sent_tokenize(text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(k, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary

def app():
    title = st.title("Text Summarization")
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6, row1_col7, row1_col8 = st.columns(8)

    with row1_col1:
        if st.button('Wikipedia Page'):
            webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Automatic_summarization')

    with row1_col2:
        if st.button("Google it"):
            webbrowser.open_new_tab("https://www.google.com/search?q=text+summarization")

    # st.text(title.replace(' ', '+'))
    # st.title
    with st.expander("See Explanation"):
        st.markdown("""
        ### Description of the Task:
        Automatic summarization is the process of shortening a set of data computationally, to create a subset (a summary)
        that represents the most important or relevant information within the original content. 
          
        ### Description of the Output:  
        Text Summarization can be **abstractive** or **extractive**. **Abstractive** text summarization will synthesize new 
        text from the input text, just like a human would. **Extractive** text summarization will identify common words 
        in the text, and return a specified number of sentences ranked in order of importance.  
          
        This tool is using **extractive** text summarization - If you're looking for an Abstractive solution, google "Google Pegasus".
         """)

    text = st.text_area("Put some text in the box below, to give Keyword Extraction a test drive!")

    if text:
        defMax = len(nltk.sent_tokenize(text))
    #     suggestedLen = round(defMax/4)
    else:
        defMax = 25
    suggestedLen = 3
    n_sentences = st.slider("Number of Sentences to return", min_value=1, max_value=defMax, value=suggestedLen)

    run = st.button("Run")
    if text and run:
        thing = summarize(k=n_sentences, text=text)
        for doc in nltk.sent_tokenize(thing):
            st.text("• " + doc)

if __name__ == "__main__":
    app()