from pprint import pprint
from typing import Any
import requests
from config import HOST, PORT
from models.db_filter import Filter

import pandas as pd
from io import StringIO


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
        print(type(data_str), data_str, sep="\n\n")
        if post_request:
            # TODO: TypeError: data_str['data']
            df = pd.read_json(
                StringIO(data_str['data'])
                )
        
        else:
            df = pd.read_json(
                StringIO(data_str)
                )
        
        return df
    
    except Exception as _ex:
        return _ex


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
            return data
        
        return respo.status_code
    
    except Exception as e:
        return e
    
    
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
    

filter = Filter(
    limit=5
)


data = get_by_filter(filter=filter)
print(data.columns)

# data = get_all_data()
# pprint(data.head(5))