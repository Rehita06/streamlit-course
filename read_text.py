import streamlit as st
import pandas as pd

# Page title
st.title("Local File Reader")

# Read and display TXT file

st.header("Text File")

with open("sample.txt", "r") as file:
    text_content = file.read()

st.text(text_content)