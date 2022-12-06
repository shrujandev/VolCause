import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_members, get_details, edit_details, set_age, set_count


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=[
                      'Member_ID', 'Name', 'Gender', 'DOB', 'Age', 'Blood Group', 'Address'])
    with st.expander("Current Data"):
        st.dataframe(df)
    list_of_members = [i[0] for i in view_only_members()]
    selected_member = st.selectbox("Members to update", list_of_members)
    selected_result = get_details(selected_member)

    if selected_result:
        Member_ID = selected_result[0][0]
        Name = selected_result[0][1]
        Gender = selected_result[0][2]
        DOB = selected_result[0][3]
        Age = selected_result[0][4]
        Blood_group = selected_result[0][5]
        Address = selected_result[0][6]

        col1, col2 = st.columns(2)
        with col1:
            new_memberID = st.number_input("Member ID", Member_ID)
            new_name = st.text_input("Name", Name)
            new_gender = st.radio("Gender", ["Male", "Female"])
        with col2:
            new_dob = st.text_input("DOB", DOB)
            new_blood = st.selectbox(
                "Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
            new_address = st.text_area("Address", Address)

        if st.button("Update Members"):
            edit_details(new_memberID, new_name, new_gender,
                         new_dob, Age, new_blood, new_address, Member_ID, Name, Gender, DOB, Blood_group, Address)
            st.success("Successfully Updated Member :{}".format(Name))
        if st.button("Set Age"):
            set_age()
            st.success("Successfully set age in members")
        if st.button("Update Volunteer Count"):
            set_count()
            st.success("Successfully Updated Count")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=[
                       'Member_ID', 'Name', 'Gender', 'DOB', 'Age', 'Blood Group', 'Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)
