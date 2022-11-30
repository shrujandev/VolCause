import pandas as pd
import streamlit as st

from database import view_all_data, view_only_members, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=[
                      'Member_ID', 'Name', 'Gender', 'DOB', 'Age', 'Blood Group', 'Address'])
    with st.expander("Current Data"):
        st.dataframe(df)
    list_of_members = [i[0] for i in view_only_members()]
    selected_member = st.selectbox("Task to Delete", list_of_members)
    st.warning("Do you want to delete {}".format(selected_member))
    if st.button("Delete Member"):
        delete_data(selected_member)
        st.success("Member has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=[
                       'Member_ID', 'Name', 'Gender', 'DOB', 'Age', 'Blood Group', 'Address'])
    with st.expander("Updated Data"):
        st.dataframe(df2)
