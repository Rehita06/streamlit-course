import streamlit as st
import pandas as pd

st.title("Student Dataset Processor")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    filtered = df[df["Marks"] >= 80]
    st.subheader("Students Scoring Above 80")
    st.dataframe(filtered)

    st.write(f"Total students scoring above 80: {len(filtered)}")