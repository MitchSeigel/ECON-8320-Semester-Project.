import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#dashboard title
st.title('BLS Dashboard')

#data file call
data = pd.read_csv( "https://raw.githubusercontent.com/MitchSeigel/ECON-8320-Semester-Project./refs/heads/main/Data.csv")

data['year_month'] = data['year'].astype(str) + '_' + data['Month']

#directions above first dropdown
selected_series = st.multiselect("Select Series to Display", data["Series Name"].unique())


# x-axis
x_axis = 'year_month'

#create the chart when one or more serries are selected
if selected_series and x_axis:
    chart = alt.Chart(data[data["Series Name"].isin(selected_series)]).mark_line().encode(
            x=x_axis,
            y="value:Q",  # Specify value as quantitative
            color="Series Name:N",
            tooltip=["Series Name", "value", x_axis]
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

else: # Handle cases with no selections
    st.write("Select at least one series to display the chart.")
