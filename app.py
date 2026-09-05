import streamlit as st
st.title ("Student Pass/Fail Checker")
name = st.text_input("Enter yoour name")
marks = st.number_input("Enter Marks", min_value=0, max_value=100)
if name:
    st.write(f"Hello, {name}!")

if marks >= 50:
    st.success("Result: Pass")
else:
    st.error("Result: Fail")