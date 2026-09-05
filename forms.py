import streamlit as st

st.title("Student Pass/Fail Checker")

# Layout: split into two columns for a cleaner look
col1, col2 = st.columns(2)

with st.form("student_form"):
    with col1:
        name = st.text_input("Enter Your Name")
    with col2:
        marks = st.number_input("Enter Marks", min_value=0, max_value=100)

    submitted = st.form_submit_button("Submit")

if submitted:
    st.divider()  # visual separator between input section and result section

    if name:
        st.write(f"Hello, {name}!")

    if marks >= 50:
        st.success("Result: Pass")
    else:
        st.error("Result: Fail")