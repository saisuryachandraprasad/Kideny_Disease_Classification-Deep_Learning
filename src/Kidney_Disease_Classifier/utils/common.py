import os
from box.exceptions import BoxValueError
from src.Kidney_Disease_Classifier import logger
from pathlib import Path
from box import ConfigBox
from typing import Any
import joblib
import json
import yaml
import base64
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