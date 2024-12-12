import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#dashboard title
st.title('Customizable BLS Metrics Dashboard')

#data file call
data = pd.read_csv( "https://raw.githubusercontent.com/MitchSeigel/ECON-8320-Semester-Project./refs/heads/main/Data.csv")

#concatinate year and month in a new column for ease of use in dashboard
data['Year-Month'] = data['year'].astype(str) + '-' + data['Month']

#create a datetime column based off of Year-Month
data['Date'] = pd.to_datetime(data['Year-Month'], format='%Y-%B', errors='coerce')

#sort by the date
data = data.sort_values('Date')

#date list for drop-downs
Date = sorted(data['Date'].unique())

#create dropdowns for start and end date
start_Date = st.selectbox("Select Start Date", Date)
end_Date = st.selectbox("Select End Date", Date, index=len(Date)-1)

#filter data based on selected dates
filtered_data = data[
    (data['Date'] >= start_Date) & (data['Date'] <= end_Date)
]

#create series list for drop-down menu
available_series = sorted(filtered_data['Series Name'].unique())

#create the actual drop-down menu
selected_series = st.multiselect("Select Series to Display", available_series, default=available_series)

#filter data based on series selection
filtered_data = filtered_data[filtered_data['Series Name'].isin(selected_series)]

#create the line chart
chart = alt.Chart(filtered_data).mark_line().encode(
    x=alt.X('Date', title="Date"),
    y=alt.Y('value', title="Value"),
    color='Series Name',
    tooltip=['Series Name', 'Date', 'value']
).properties(
    width=800,
    height=400
).interactive()

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

