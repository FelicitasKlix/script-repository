import streamlit as st

def show_pmax_insights():
    st.title("Script de PMAX")
    st.write("Este script nos da insights sobre términos de búsqueda, placements, etc para las campañas de PMAX.")
    st.write("Debemos pegar en Google Ads los tres scripts que se muestran a continuación:")
    url = "https://docs.google.com/spreadsheets/d/1TL-YZSCG7QWe2UgetRdw9-_NWNDkrrm5HOQQ1goWhSU/edit#gid=526323273"
    #Hacer que se haga una copia de la url de inshgts pmax, y que esa se pegue en los archivos de pmax1.py, pmax2.py y pmax3.py

    st.subheader("PMAX v1:")
    # Agrega el contenido de tu página PMAX aquí
    script1=open("scripts/pmax1.js","r+")
    contenido1=script1.read()
    st.code(contenido1, language="javascript")
    st.subheader("PMAX v2:")
    # Agrega el contenido de tu página PMAX aquí
    script2=open("scripts/pmax2.js","r+")
    contenido2=script2.read()
    st.code(contenido2, language="javascript")
    st.subheader("PMAX v3:")
    # Agrega el contenido de tu página PMAX aquí
    script3=open("scripts/pmax3.js","r+")
    contenido3=script3.read()
    st.code(contenido3, language="javascript")