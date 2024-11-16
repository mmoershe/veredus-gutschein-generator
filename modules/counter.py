from modules.CONST import DATA_DIR

import os 
import json


def counter() -> int: 
    if not os.path.exists(DATA_DIR): 
        print(f"DATA_DIR didn't exist and will be created.")
        save_data(1)

    with open(DATA_DIR) as DATA: 
        current_counter_value: int = json.load(DATA)["counter"]

    save_data(current_counter_value+1)
    return current_counter_value


def save_data(counter: int) -> None:
    content: dict = {"counter": counter}
    with open(DATA_DIR, "w") as file: 
        json.dump(content, file)
