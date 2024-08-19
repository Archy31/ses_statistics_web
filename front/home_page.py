import streamlit as st
import pandas as pd

from map_container import data_mapping
from filter_container import data_filter
from table_container import data_table


def home():
    table_data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    map_data = pd.DataFrame({
        'lat': [49.058, 50.383, 49.599, 50.677, 53.036, 50.541, 51.524, 54.992, 49.88],
        'lon': [11.115, 12.528, 11.231, 10.408, 8.185, 8.055, 7.639, 11.636, 7.678],
        'hover': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'color_1': [3, 3, 4, 3, 5, 5, 5, 4, 2],
        'color_2': [5, 5, 3, 1, 1, 2, 5, 2, 2],
        'color_3': [3, 2, 1, 5, 3, 2, 5, 2, 2]
    })
    
    col1, col2 = st.columns([7, 7])
    
    with col1:
        data_filter()
    
    with col2:
        data_mapping(data=map_data)
        
    data_table(table_data)