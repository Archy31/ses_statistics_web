from pprint import pprint
from typing import Any, Iterable
import requests
from config import HOST, PORT
from models.db_filter import Filter

import pandas as pd
from io import StringIO
import streamlit as st


URL = f"http://{HOST}:{PORT}/events"



def __bytes2df(data: bytes, post_request: bool = False) -> pd.DataFrame | Exception:
    """To get pandas DataFrame from bytes.

    Args:
        data (bytes): _description_

    Returns:
        pd.DataFrame | Exception: _description_
    """
    try:
        data_str = data.decode('utf-8')
        if post_request:
            # TODO: TypeError: data_str['data']
            df = pd.read_json(
                StringIO(data_str)
                )
            df = pd.DataFrame(df['data'].tolist())
        
        else:
            df = pd.read_json(
                StringIO(data_str)
                )
        
        return df
    
    except Exception as _ex:
        return _ex
    

def __format_date_time(data: pd.DataFrame) -> Any:
    try:
        data['reg_date'] = data['reg_date'].apply(
                lambda x: x.split('T')[0] if pd.notnull(x) else None
            )
            
        data['reg_time'] = data['reg_time'].apply(
            lambda x: x.split('T')[1][:-1] if pd.notnull(x) else None
        )
        
        data['last_phase_time'] = data['last_phase_time'].apply(
            lambda x: x.split('T')[1][:-1] if pd.notnull(x) else None
        )
        
        return data
    
    except Exception as __ex:
        return __ex


def __format_float_nums(data: pd.DataFrame, columns: Iterable[float]) -> Any:
    try:
        for col in columns:
            data[col] = data[col].apply(
                    lambda x: f"{x:.1f}" if pd.notnull(x) else None
                )
        
        return data
    
    except Exception as __ex:
        return __ex
    

def __format_str(data: pd.DataFrame, columns: Iterable[float]) -> Any:
    try:
        for col in columns:
            data[col] = data[col].apply(
                    lambda x: f"{x:.5f}" if pd.notnull(x) else None
                )
        
        return data
    
    except Exception as __ex:
        return __ex


@st.cache_data
def get_all_data(url: str = URL) -> Any:
    """To get all table data.

    Args:
        url (str, optional): _description_. Defaults to url.

    Returns:
        Any: _description_
    """
    try:
        respo = requests.get(url=url)
        if respo.status_code == 200:
            data = __bytes2df(respo.content)    
            data = __format_date_time(data=data) 
            data = __format_float_nums(data=data, columns=['magnitude'])  
            data = __format_str(data=data, columns=['latitude', 'longitude'])     
            
            return data
        
        return respo.status_code
    
    except Exception as e:
        return e
    

@st.cache_data
def get_by_filter(filter: Filter, url: str = URL) -> Any:
    """To get data by filter.

    Args:
        filter (Filter): _description_
        url (str, optional): _description_. Defaults to url.

    Returns:
        Any: _description_
    """
    
    filter = {
        "limit": filter.limit,
        "offset": filter.offset,
        "sort_by": {
            "column": filter.sort_by.column,
            "order": filter.sort_by.order
        },
        "search": {
            "column": filter.search.column,
            "value": filter.search.value
        }
    }
    
    try:
        respo = requests.post(url=url, json=filter)
        if respo.status_code == 200:
            data = __bytes2df(respo.content, post_request=True)
            return data
        
        return respo.status_code
    
    except Exception as e:
        return e
    
