import streamlit as st
from datetime import date, time
from time import sleep


def __from_date_time(form: st) -> tuple[date, time]:
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
        

def __until_date_time(form: st) -> tuple[date, time]:
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
        

def __filter_by_datetime(form: st):
    __from_date_time(form=form)
    __until_date_time(form=form)


def __stream_data(data: str, delay: float = 0.03):
    for l in data:
        yield l
        sleep(delay)


def __circle_area(form: st) -> tuple[float, float, float]:
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


def __quadrangle_area(form: st):
    pass


def __filter_by_area(form: st):
    areas = {
        "Circle": __circle_area,
        "Quadrangle": __quadrangle_area,
    }

    area = form.selectbox(
        "Select area type:",
        ("Not selected", "Circle", "Quadrangle"),
    )

    if area in areas.keys():
        areas[area](form)


def __filter_by_mag(form: st) -> tuple[float, float]:
    forms = form.columns(2)
    min_mag = forms[0].number_input("Min magnitude", min_value=0.0, max_value=12.0, value=3.5, format="%0.1f")
    max_mag = forms[1].number_input("Max magnitude", min_value=0.0, max_value=12.0, value=8.0, format="%0.1f")

    return min_mag, max_mag


def data_filter():
    base_container = st.container(border=True)

    base_container.write("**By date & time:**")
    ctr_date_time = base_container.container(border=True)
    __filter_by_datetime(form=ctr_date_time)

    base_container.write("**By area:**")
    ctr_area = base_container.container(border=True)
    __filter_by_area(form=ctr_area)

    base_container.write("**By magnitude:**")
    ctr_mag = base_container.container(border=True)
    __filter_by_mag(form=ctr_mag)

    # base_container.button(label="Search 🔎️")
    # search = base_container.form_submit_button(
    #     label="Search 🔎️",
    #     help="Search data by chosen filters.",
    #     use_container_width=True
    # )