import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file: {path_to_yaml}")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, versbose=True):
    """
    Creates directories if they don't exist.
    """
    for directory in path_to_directories:
        directory = Path(directory)
        if not directory.is_dir():
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {directory}")