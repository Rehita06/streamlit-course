import streamlit as st
import pandas as pd

st.title("Student Marks Viewer")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Here is your data:")
    st.dataframe(df)

    average_marks = df["Marks"].mean()

    st.write("Filter students by minimum marks:")
    min_marks = st.slider("Minimum Marks", 0, 100, 50)

    filtered_df = df[df["Marks"] >= min_marks]
    st.write(f"Students with marks {min_marks} or above:")
    st.dataframe(filtered_df)

    st.write(f"Average Marks: {average_marks:.2f}")