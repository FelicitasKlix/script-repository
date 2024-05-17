#dispositivos.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import datetime
from streamlit_echarts import st_echarts

def pmax():
    st.title("PMAX Script")
    script=open("scripts/pmax1.py","r+")
    contenido=script.read()
    st.code(contenido, language="javascript")
