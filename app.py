import streamlit as st
st.title ("Student Pass/Fail Checker")
name = st.text_input("Enter your name")
marks = st.number_input("Enter Marks", min_value=0, max_value=100)
attendance_ok = st.checkbox("Attendance requirement met")
if st.button("Evaluate"):
    if name:
        st.write(f"Hello, {name}!")

    if marks >= 50 and attendance_ok:
        st.success("Result: Pass")
    else:
        st.error("Result: Fail")

