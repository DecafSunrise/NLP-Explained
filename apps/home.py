import streamlit as st


def app():
    st.title("Learn about NLP")

    st.markdown(
        """
        This web app demonstrates various Natural Language Processing (NLP) techniques.
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