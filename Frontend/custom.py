import streamlit as st
import pandas as pd
from database import ret_query


def custom():
    command = st.text_area("Enter Query")
    words = command.split(" ")
    if words[0] == "DROP":
        st.warning("Not Authorised to DROP tables")
    if (st.button("Submit Query")):
        err, message, cols = ret_query(command)
        if err:
            st.warning(message)
        else:
            df = pd.DataFrame(message, columns=cols)
            with st.expander("Query Result"):
                st.dataframe(df)
