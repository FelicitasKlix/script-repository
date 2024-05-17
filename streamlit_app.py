# streamlit_app.py

import streamlit as st
import streamlit_authenticator as stauth

from pages.pmax import pmax


def main():

    with st.sidebar:
        #st.sidebar.title("Welcome {name}")
        st.header("Scripts Repository")
        api_options = ("PMAX", "Dispositivos", "Objetivos")
        selected_api = st.sidebar.radio(
            label="Choose your preferred view:",
            options=api_options,
        )

    if(selected_api == "PMAX"):
        pmax()


if __name__ == "__main__":
    main()
