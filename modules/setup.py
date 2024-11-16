from modules.CONST import OUTPUT_DIR

import os


def setup() -> None: 
    generate_directories([OUTPUT_DIR])


def generate_directories(directories: list) -> None: 
    for directory in directories: 
        if not os.path.exists(directory): 
            os.makedirs(directory)
            print(f"Created the following missing Directory: {directory}")
