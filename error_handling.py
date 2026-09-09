import streamlit as st

st.title("Student Result Checker")

name = st.text_input("Enter Name")
marks = st.number_input("Enter Marks", min_value=-100)

if name:
    if 0 <= marks <= 100:
        if marks >= 50:
            st.success(f"{name} has Passed")
        else:
            st.error(f"{name} has Failed")
    else:
        st.warning("⚠️ Please enter marks between 0 and 100 to see a result.")
else:
    st.info("👋 Please enter your name to get started.")