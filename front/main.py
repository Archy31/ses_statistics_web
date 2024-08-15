import streamlit as st
import json, requests



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
