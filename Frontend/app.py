import mysql.connector
import streamlit as st
from create import create
from delete import update
from read import read
from delete import delete
from update import update


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    datebase="volcause_415"
)

c = mydb.cursor()
c.execute("USE volcause_415")
c.close()


def main():
    st.title("VolCause")
    menu = ["ADD", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice = "ADD":
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
    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
