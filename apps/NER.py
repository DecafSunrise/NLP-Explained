import streamlit as st
import webbrowser
import spacy
nlp=spacy.load('en_core_web_sm')

def app():
    title = st.title("Keyword Extraction")
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6, row1_col7, row1_col8 = st.columns(8)

    with row1_col1:
        if st.button('Wikipedia Page'):
            webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Named-entity_recognition')

    with row1_col2:
        if st.button("Google it"):
            webbrowser.open_new_tab("https://www.google.com/search?q=named+entity+recognition")

    # st.text(title.replace(' ', '+'))
    # st.title
    with st.expander("See Explanation"):
        st.markdown("""
        ### Description of the Task:
        **Named-entity recognition (NER)** (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

        ### Description of the Output:  
        This page uses the SpaCy python library, and the default en_core_web_sm model. The output will print the hit term, and the category associated (Noun, organization, etc)
         """)

    # st.text("")
    text = st.text_area("Put some text in the box below, to give Keyword Extraction a test drive!")

    if st.button("Run"):
        doc = nlp(text)
        # st.text(keywords)
        for ent in doc.ents:
            st.text(f"{ent.text}, {ent.label_}")


if __name__ == "__main__":
    app()