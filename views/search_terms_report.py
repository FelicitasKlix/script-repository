import streamlit as st

def show_search_terms_report():
    st.title("Search Term Report (last 30 days)")
    st.write("Este script enviará un mail con un reporte de los términos de búsqueda encontrados, para cada campaña y adgorup activo, que haya convertido y generado impresiones en los últmos 30 días")
    st.write("Debemos pegar en Google Ads el script que se muestra a continuación:")
    user_email = st.text_input("Ingrese su correo electrónico:")
    
    # Agrega el contenido de tu página PMAX aquí
    script=open("scripts/search_terms_30d_report.js","r+")
    contenido=script.read()

    # Replace the yourEmail variable with the user's input
    updated_script_content = contenido.replace("var yourEmail = \"\";", f"var yourEmail = \"{user_email}\";")

    # Display the updated script content
    st.code(updated_script_content, language="javascript")