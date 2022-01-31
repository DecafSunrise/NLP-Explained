import streamlit as st

def app():
    st.title("Learn about NLP")

    st.markdown(
        """
        **Natural language processing (NLP)** is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.
        
        Want to explore some common NLP tasks? Click on the tools to the left, and give them a try.
        """
    )

    st.info("Click on the left sidebar menu to navigate to the different apps.")
# app()
    # st.subheader("Timelapse of Satellite Imagery")
    # st.markdown(
    #     """
    #     The following timelapse animations were created using the Timelapse web app. Click `Create Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
    # """
    # )

    # row1_col1, row1_col2 = st.columns(2)
    # with row1_col1:
    #     st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    #     st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")
    #
    # with row1_col2:
    #     st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    #     st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")