import streamlit as st
import pandas as pd
import json

st.title("Module Summary App")

# ---- File Formats + File Upload ----
st.header("1. File Upload & File Formats")
file_type = st.selectbox("Choose file type", ["CSV", "JSON"])
uploaded_file = st.file_uploader(f"Upload a {file_type} file")

if uploaded_file is not None:

    # ---- Pandas (CSV handling) ----
    if file_type == "CSV":
        df = pd.read_csv(uploaded_file)

        st.header("2. Pandas — Displaying Data")
        st.dataframe(df)

        # ---- Data Cleaning ----
        st.header("3. Data Cleaning")
        st.write("Missing values per column:")
        st.write(df.isnull().sum())
        df["Marks"] = df["Marks"].fillna(0)
        st.write("After filling missing Marks with 0:")
        st.dataframe(df)

        # ---- File Processing ----
        st.header("4. File Processing — Filtering")
        filtered = df[df["Marks"] >= 50]
        st.write("Students scoring 50 or above:")
        st.dataframe(filtered)

    # ---- JSON ----
    elif file_type == "JSON":
        data = json.load(uploaded_file)

        st.header("2. JSON — Structured Data")
        st.json(data)

        st.header("3. Extracting Specific Values")
        for key in data:
            st.write(f"{key}: {data[key]}")