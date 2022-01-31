import streamlit as st
import webbrowser
import spacy
nlp=spacy.load('en_core_web_sm')
from annotated_text import annotated_text

## https://github.com/streamlit/example-app-document-anonymizer/blob/main/app.py

def process_text(doc, selected_entities, anonymize=False):
    tokens = []
    for token in doc:
        if (token.ent_type_ == "PERSON") & ("PER" in selected_entities):
            tokens.append((token.text, "Person", "#faa"))
        elif (token.ent_type_ in ["GPE", "LOC"]) & ("LOC" in selected_entities):
            tokens.append((token.text, "Location", "#fda"))
        elif (token.ent_type_ == "ORG") & ("ORG" in selected_entities):
            tokens.append((token.text, "Organization", "#afa"))
        else:
            tokens.append(" " + token.text + " ")

    if anonymize:
        anonmized_tokens = []
        for token in tokens:
            if type(token) == tuple:
                anonmized_tokens.append(("X" * len(token[0]), token[1], token[2]))
            else:
                anonmized_tokens.append(token)
        return anonmized_tokens

    return tokens

def app():
    title = st.title("Named Entity Recognition")
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
        This page uses the SpaCy python library, and the default en_core_web_sm model. This tool "pretty prints" the input, with 
        the hit terms color coded, and tagged with their accociated label (Noun, organization, etc). For better tagging accuracy,
        it's advisable to fine-tune the NER model on your specific task (Finance, Biology, Defense, etc).
         """)

    # st.text("")
    text = st.text_area("Put some text in the box below, to give Named Entity Recognition a go!")

    if st.button("Run"):
        doc = nlp(text)
        selected_entities = ["LOC", "PER", "ORG"]
        tokens = process_text(doc, selected_entities)

        annotated_text(*tokens)


if __name__ == "__main__":
    app()