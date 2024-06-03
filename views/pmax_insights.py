import streamlit as st
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# Google Sheets URL to copy
SHEET_URL = "https://docs.google.com/spreadsheets/d/1yP0TS40jNBaNSpTkxBD8lfjvLSTu9qboC9vSaPTw5RU/edit?usp=sharing"

def show_pmax_insights():
    st.title("Script de PMAX")
    st.write("Este script nos da insights sobre términos de búsqueda, placements, etc para las campañas de PMAX.")
    st.write("Debemos pegar en Google Ads los tres scripts que se muestran a continuación:")

    st.subheader("PMAX v1:")
    #new_url = copy_file()
    #st.subheader(new_url)
    # Agrega el contenido de tu página PMAX aquí
    script1=open("scripts/pmax1.js","r+")
    contenido1=script1.read()
    #updated_script_content1 = contenido1.replace("let sheetUrl = = \"\";", f"let sheetUrl = = \"{new_url}\";")
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


def authenticate_gdrive():
    service = build('drive', 'v3', credentials=credentials)
    return service

def copy_file():
    # # Build the Drive API client
    # drive_service = build('drive', 'v3', credentials=credentials)

    # # Extract the file ID from the sheet URL
    # file_id = SHEET_URL.split("/")[5]

    # # Create a copy of the file
    # copy_request = drive_service.files().copy(fileId=file_id).execute()

    # # Get the URL of the copied file
    # copied_file_url = f"https://docs.google.com/spreadsheets/d/{copy_request['id']}"

    # return copied_file_url
    # Build the Drive API client
    drive_service = authenticate_gdrive()

    # Extract the file ID from the sheet URL
    file_id = SHEET_URL.split("/")[5]

    # Create a copy of the file
    copy_request = drive_service.files().copy(fileId=file_id).execute()

    # Get the URL of the copied file
    copied_file_id = copy_request['id']
    copied_file_url = f"https://docs.google.com/spreadsheets/d/{copied_file_id}"

    # Set permissions to "anyone with the link"
    permission = {
        'type': 'anyone',
        'role': 'reader'
    }
    drive_service.permissions().create(
        fileId=copied_file_id,
        body=permission
    ).execute()

    return copied_file_url