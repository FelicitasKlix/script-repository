import streamlit as st
from views.pmax_insights import show_pmax_insights
from views.utm_creator_gads import show_utm_creator_gads
from views.search_terms_report import show_search_terms_report


def main():
    # Configuración del título de la aplicación
    st.set_page_config(page_title="Script Repository", layout="wide")

    with st.sidebar:
        #st.sidebar.title("Welcome {name}")
        st.header("Script Repository")
        api_options = ("PMAX Insights", "UTM Generator", "Search Terms Report")
        selected_api = st.selectbox(
            label="Choose script:",
            options=api_options,
        )

    if(selected_api == "PMAX Insights"):
        show_pmax_insights()
    elif(selected_api == "UTM Generator"):
        show_utm_creator_gads()
    elif(selected_api == "Search Terms Report"):
        show_search_terms_report()


if __name__ == "__main__":
    main()