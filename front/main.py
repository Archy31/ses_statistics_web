import streamlit as st
import json, requests
from streamlit_globe import streamlit_globe



st.title("Seismikalyk Eskertuu Systemasy")

option = st.selectbox(
    "Select DataBase:",
    ("SES (ЦАИИЗ)", "USGS", "НАН КР", "НАН УзР", "НАН КазР")
)

st.write("")
st.write("Select the date interval from slider below 👇️")
x = st.slider("Start date:", 2016, 2024, step=1)
y = st.slider("End date:", 2023, 2024)

inputs = {
    "operation": option,
    "x": x,
    "y": y
}

if st.button("Search"):
    res = requests.post(
        url="http://127.0.0.1:8000/data",
        data=json.dumps(inputs)
    )
    
    st.subheader(f"Response = {res.text}")

st.subheader("Globe")
pointsData=[{'lat': 49.19788311472706, 'lng': 8.114625722364316, 'size': 0.3, 'color': 'red'}]
labelsData=[{'lat': 49.19788311472706, 'lng': 8.114625722364316, 'size': 0.3, 'color': 'red', 'text': 'Landau'}]
streamlit_globe(pointsData=pointsData, labelsData=labelsData, daytime='day', width=800, height=600)