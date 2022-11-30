import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_events, view_all_data


def read():
    result = view_events()
    df = pd.DataFrame(result, columns=['Event_ID', 'Event_Name', 'Manager_ID',
                      'Event_Type', 'Event_Date', 'Venue', 'Volunteer_Count', 'Org_ID'])
    with st.expander("All Events"):
        st.dataframe(df)
    with st.expander("Event Details"):
        event_df = df[['Volunteer_Count', 'Event_Name']].copy()
        st.dataframe(event_df)
        count_name = event_df.Volunteer_Count.values.tolist()
        event_name = event_df.Event_Name.values.tolist()
        p1 = px.pie(event_df, names=event_name, values=count_name)
        st.plotly_chart(p1)
