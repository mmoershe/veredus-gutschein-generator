from modules.setup import setup 
from modules.code import generate_code
from modules.tkinter import ask_for_price_gui
from modules.generation import generate_gift_card
from modules.CONST import OUTPUT_FILE_DIR

from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__": 
    setup()
    price: int = ask_for_price_gui()
    code: str = generate_code()
    date_text: str = datetime.today().strftime('%d-%m-%Y')
    generate_gift_card(price, code, date_text)
    
    SECONDARY_OUTPUT_DIR: str | None = os.getenv("SECONDARY_OUTPUT_DIR")
    if SECONDARY_OUTPUT_DIR: 
        import shutil
        try:
            shutil.copy(OUTPUT_FILE_DIR, SECONDARY_OUTPUT_DIR)
        except: 
            print("Failed to copy output to secondary_output")
