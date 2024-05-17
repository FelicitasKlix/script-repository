import streamlit as st
import streamlit_authenticator as stauth

st.title("Script Repository")

code = """
def hello():
    print("Hello, Streamlit!")

hello()
"""

st.code(code, language='python')