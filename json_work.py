import streamlit as st
import json

st.title("JSON Data Viewer")

uploaded_file = st.file_uploader("Upload your JSON file", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)

    st.write("Here is your JSON data:")
    st.json(data)

    st.write("Extracted values:")
    st.write("Name:", data["name"])
    st.write("Age:", data["age"])
    st.write("Course:", data["course"])