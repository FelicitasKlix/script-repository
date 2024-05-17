#dispositivos.py

import streamlit as st

def pmax():
    st.title("PMAX Script")
    script=open("/scripts/pmax1.py","r+")
    contenido=script.read()
    st.code(contenido, language="javascript")
