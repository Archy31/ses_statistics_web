import streamlit as st
import pandas as pd

from map_container import data_mapping
from filter_container import data_filter
from table_container import data_table
from data_fisher import get_by_filter, get_all_data
from models.db_filter import Filter, Search
from statistics_page import statistics



def home():
    # table_data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    filter = Filter(
        search=Search(column="event_status", value="Новое")
    )
    # table_data = get_by_filter(filter=filter)
    table_data = get_all_data()
    
    chart_data = table_data.groupby('magnitude').size().reset_index(name='Count')
    chart_data.rename(columns={'magnitude': 'Magnitude'}, inplace=True)   
    
    map_data = pd.DataFrame({
        'lat': [42.85412262672435],
        'lon': [74.5333091110194],
        'hover': ["CAIAG (ЦАИИЗ)"]
    })
    
    with st.container(border=True):
        col1, col2 = st.columns([7, 7])
        
        with col1:
            data_filter()
        
        with col2:
            data_mapping(data=map_data)
        
    with st.container(border=True):
        col1, col2 = st.columns([7, 7])
        
        with col1:
            data_table(table_data)
            
        with col2:
            ctr = st.container(border=True)
            statistics(form=ctr, data=chart_data)
