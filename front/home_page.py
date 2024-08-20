import streamlit as st
import pandas as pd

from map_container import data_mapping
from filter_container import data_filter
from table_container import data_table


def home():
    table_data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    map_data = pd.DataFrame({
        'lat': [42.85412262672435],
        'lon': [74.5333091110194],
        'hover': ["CAIAG (ЦАИИЗ)"],
    })
    
    col1, col2 = st.columns([7, 7])
    
    with col1:
        data_filter()
    
    with col2:
        data_mapping(data=map_data)
        
    data_table(table_data)