import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#dashboard title
st.title('Customizable BLS Metrics Dashboard')

#data file call
data = pd.read_csv( "https://raw.githubusercontent.com/MitchSeigel/ECON-8320-Semester-Project./refs/heads/main/Data.csv")

#concatinate year and month in a new column for ease of use in dashboard
data['year_month'] = data['year'].astype(str) + '_' + data['Month']

# Dropdown for Series Names
selected_series = st.multiselect(
    "Select Series Names to display:",
    data['Series Name'].unique(),
    default=data['Series Name'].unique()  # Default to all series
)

# Dropdowns for Year-Month
year_month_options = sorted(data["year_month"].unique())
selected_x_start = st.selectbox("Select Start Year-Month", year_month_options)
selected_x_end = st.selectbox("Select End Year-Month", year_month_options)

# Filter data based on series name selections and year-month selections
filtered_df = data[data['Series Name'].isin(selected_series)]
start_index = year_month_options.index(selected_x_start)
end_index = year_month_options.index(selected_x_end)
filtered_df = filtered_df[filtered_df["year_month"].isin(year_month_options[start_index : end_index+1])]

# Create the line chart
chart = alt.Chart(filtered_df).mark_line().encode(
    x=alt.X('year_month', title="Year-Month", sort=year_month_options),
    y=alt.Y('value', title="Value"),
    color='Series Name',
    tooltip=['Series Name', 'year_month', 'value']
).properties(
    width=600,
    height=400
).interactive()

# Display the chart
st.altair_chart(chart, use_container_width=True)
