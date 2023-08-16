import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")
 
# Import your data
file='dados/IDH.xlsx'
df=pd.read_excel(file, sheet_name="Base")
 
# Paste the copied Pygwalker chart code here
vis_spec = """<PASTE_COPIED_CODE_HERE>"""
 
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, spec=vis_spec, return_html=True)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)