import streamlit as st
import pandas as pd

# Page title
st.title("Local File Reader")

st.header("CSV File")

df = pd.read_csv("sample1.csv")

st.dataframe(df)