# streamlit_app.py

import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

from views.pmax import pmax


def main():

    with st.sidebar:
        #st.sidebar.title("Welcome {name}")
        st.header("Scripts Repository")
        api_options = ("PMAX", "Dispositivos", "Objetivos")
        selected_api = st.selectbox(
            label="Choose your preferred view:",
            options=api_options,
        )

    if(selected_api == "PMAX"):
        pmax()


if __name__ == "__main__":
    main()