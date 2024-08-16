from cProfile import label

import streamlit as st
from jsonschema.benchmarks.const_vs_enum import value
from st_aggrid import AgGrid
from streamlit_plotly_mapbox_events import plotly_mapbox_events
import plotly.express as px

import pandas as pd
from enum import Enum
from datetime import date, time
from time import sleep


class Layers(Enum):
    terrain: str = 'http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}'
    hybrid: str = 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}'
    satellite: str = 'http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}'


def data_table(data: pd.DataFrame):
    AgGrid(data, height=600)
    

def global_map(data: pd.DataFrame, layer: Layers = Layers.hybrid):

    mapbox = px.scatter_mapbox(
        data_frame=data, 
        lat="lat", lon="lon", 
        hover_name="hover",
        zoom=5.5, 
        height=600
        )
    
    mapbox.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "Kyrgyzstan. Bishkek. CAIAG",
                "source": [
                    layer.value
                ]
            }
        ])
    mapbox.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

    mapbox_events = plotly_mapbox_events(
        mapbox,
        click_event=True,
        select_event=True,
        hover_event=True,
        override_height=600
    )


def from_date_time(form: st) -> tuple[date, time]:
    forms = form.columns(2)
    
    fdate = forms[0].date_input(
        label='**From:**',
        value=None,
        key=0
        )
    
    ftime = forms[1].time_input(
        label='',
        value=None,
        key=1
    )
    
    return fdate, ftime
        

def until_date_time(form: st) -> tuple[date, time]:
    forms = form.columns(2)
    
    udate = forms[0].date_input(
        label='**Until:**',
        value=None,
        key=2
        )           
    
    utime = forms[1].time_input(
        label='',
        value=None,
        key=3
    )
        
    return udate, utime
        

def filter_by_datetime(form: st):
    from_date_time(form=form)
    until_date_time(form=form)

def stream_data(data: str, delay: float = 0.03):
    for l in data:
        yield l
        sleep(delay)

def circle_area(form: st) -> tuple[float, float, float]:
    """
    Read Latitude, Longitude and Radius:
    :param form: Streamlit object.
    :return: lat, long, rad
    """
    forms = form.columns(2)

    forms0 = forms[0].container(border=True)
    lat = forms0.number_input("Latitude", min_value=-90.0, max_value=90.0, value=42.8746, format="%0.5f")
    long = forms0.number_input("Longitude", min_value=-180.0, max_value=180.0, value=74.5698, format="%0.5f")
    rad = forms[1].number_input("Radius (km)", value=200.0)

    return lat, long, rad

def quadrangle_area(form: st):
    pass


def lasso_area(form: st):
    pass


def filter_by_area(form: st):
    areas = {
        "Circle": circle_area,
        "Quadrangle": quadrangle_area,
        "Lasso": lasso_area
    }

    area = form.selectbox(
        "Choose the type of area:",
        ("Not selected", "Circle", "Quadrangle", "Lasso"),
    )

    if area in areas.keys():
        areas[area](form)


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
        data_filter = st.container(border=True)

        data_filter.write("**By date & time:**")
        ctr_date_time = data_filter.container(border=True)
        filter_by_datetime(form=ctr_date_time)

        data_filter.write("**By area:**")
        ctr_area = data_filter.container(border=True)
        filter_by_area(form=ctr_area)
        # data_filter.button(label="Search 🔎️")
        # search = data_filter.form_submit_button(
        #     label="Search 🔎️",
        #     help="Search data by chosen filters.",
        #     use_container_width=True
        # )

    
    with col2:
        global_map(data=map_data, layer=Layers.satellite)
        
    data_table(table_data)