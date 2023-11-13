import os
from box.exceptions import BoxValueError
from src.Kidney_Disease_Classifier import logger
from pathlib import Path
from box import ConfigBox
from typing import Any
import yaml
import base64
import json
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:

    """ read content in yaml file
    ARGS: path_to_yaml -> yaml file 
    return type configbox
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading data is completed form {path_to_yaml}")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directory:list, verbose = True):
    """ Create directory

    ARGS: list of directory to create 
    """

    for directory in path_to_directory:
        os.makedirs(directory, exist_ok= True)
        

        if verbose:
            logger.info(f"Directory is created for {directory}")


@ensure_annotations
def get_size(path: Path) ->str:
    """ get size of file
    ARGS: take path of file if already exist
    RETURN: return the str after calculating size
    """
    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} kb"


@ensure_annotations
def save_json(path:Path, data:dict):
    """This method responsible to save in json format

    args: path where to save 
    data: forrmat data to be saved
    """
    with open(path, "w") as path_obj:
        json.dump(data,path_obj,indent=4)

        logger.info(f"data is saved in {path}")


@ensure_annotations
def load_json(path:Path):
    """this method is responsible to load from json file

    args: path from where data should be loaded
    """

    with open(path) as path_obj:
        content = json.load(path_obj)
    logger.info(f"data is loaded from {path}")
    return ConfigBox(content)