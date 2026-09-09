import streamlit as st
import pandas as pd

st.title("Data Cleaning Example")

df = pd.read_csv("students.csv")

st.subheader("Original Data")
st.dataframe(df)

# Identify missing values
st.subheader("Missing Values Check")
st.write(df.isnull().sum())

# Handle missing values
df["Marks"] = df["Marks"].fillna(0)

# Transform names to uppercase
df["Name"] = df["Name"].str.upper()

st.subheader("Cleaned Data")
st.dataframe(df)