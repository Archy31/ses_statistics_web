import yaml
from typing import Any


yaml_PATH = "./config.yaml"


def get_config(path: str = yaml_PATH) -> Any:
    """To read yaml file.

    Args:
        block (str): _description_
        path (str, optional): _description_. Defaults to yaml_PATH.

    Returns:
        Any: _description_
    """
    try:
        with open(path, 'r') as file:
            config = yaml.full_load(file)
            return config
        
    except Exception as e:
        return e