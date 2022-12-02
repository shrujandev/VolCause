import mysql.connector
import streamlit as st
from create import create
from read import read
from delete import delete
from update import update
from database import create_table
from custom import custom


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="volcause_415"
)

c = mydb.cursor()
c.execute("USE volcause_415")
c.close()


def main():
    st.title("VolCause")
    menu = ["Register", "View", "Edit", "Remove", "Custom"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Register":
        st.subheader("Enter details:")
        create()
    elif choice == "View":
        st.subheader("View Member Details")
        read()
    elif choice == "Edit":
        st.subheader("Update Member Details")
        update()
    elif choice == "Remove":
        st.subheader("Delete Member Details")
        delete()
    elif choice == "Custom":
        st.subheader("Custom SQL Query")
        custom()
    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
