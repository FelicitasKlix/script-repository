#dispositivos.py

import streamlit as st

def pmax():
    st.title("PMAX Script")
    script=open("scripts/pmax1.js","r+")
    contenido=script.read()
    st.code(contenido, language="javascript")
