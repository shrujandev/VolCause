import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        memberID = st.number_input("Member ID")
        name = st.text_input("Name")
        gender = st.radio("Gender", ["Male", "Female"])
    with col2:
        dob = st.date_input("DOB")
        blood = st.selectbox(
            "Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        address = st.text_area("Address")

    if st.button("ADD Members"):
        add_data(memberID, name, gender, dob, blood, address)
        st.success("Successfully added Member :{}".format(name))
