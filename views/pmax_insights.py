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

    st.write("Debemos realizar una copia de la siguiente hoja de cálculo.")
    copy_url = 'https://docs.google.com/spreadsheets/d/1yP0TS40jNBaNSpTkxBD8lfjvLSTu9qboC9vSaPTw5RU/copy'
    st.link_button(label="Copiar Sheet", url=copy_url)
    final_url = st.text_input("Ingrese la url de la hoja de calculo:")

    #st.button("Copiar url", on_click=copy_and_update_script("scripts/pmax1.js"))
    st.write("Debemos pegar en Google Ads los tres scripts que se muestran a continuación:")

    st.subheader("PMAX v1:")
    # Agrega el contenido de tu página PMAX aquí
    script1=open("scripts/pmax1.js","r+")
    contenido1=script1.read()
    # Replace the yourEmail variable with the user's input
    updated_script_content1 = contenido1.replace("let sheetUrl = \"\";", f"let sheetUrl = \"{final_url}\";")
    st.code(updated_script_content1, language="javascript")
    st.subheader("PMAX v2:")
    # Agrega el contenido de tu página PMAX aquí
    script2=open("scripts/pmax2.js","r+")
    contenido2=script2.read()
    updated_script_content2 = contenido2.replace("let sheetUrl = \"\";", f"let sheetUrl = \"{final_url}\";")
    st.code(updated_script_content2, language="javascript")
    st.subheader("PMAX v3:")
    # Agrega el contenido de tu página PMAX aquí
    script3=open("scripts/pmax3.js","r+")
    contenido3=script3.read()
    updated_script_content3 = contenido3.replace("let sheetUrl = \"\";", f"let sheetUrl = \"{final_url}\";")
    st.code(updated_script_content3, language="javascript")


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

    print(f"Copied file URL: {copied_file_url}")
    return copied_file_url


def update_script_with_url(file_path, new_url):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace("let sheetUrl = = \"\";", f"let sheetUrl = = \"{new_url}\";")

    with open(file_path, 'w') as file:
        file.write(updated_content)

def copy_and_update_script(file_path):
    updated_url = copy_file()
    update_script_with_url(file_path, updated_url)