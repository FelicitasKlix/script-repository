import streamlit as st

def show_utm_creator_gads():

    st.title("Creador de UTMs para Google Ads")
    st.write("Con este script se crearán los parámetros a nivel Ad Group, y a nivel campaña para PMAX")
    st.write("Debemos pegar en Google Ads el script que se muestra a continuación:")
    # Agrega el contenido de tu página PMAX aquí
    script=open("scripts/utm_creator.js","r+")
    contenido=script.read()
    st.code(contenido, language="javascript")