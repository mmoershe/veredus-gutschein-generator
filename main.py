from modules.setup import setup 
from modules.code import generate_code
from modules.tkinter import ask_for_price_gui
from modules.generation import generate_gift_card


from datetime import datetime


if __name__ == "__main__": 
    setup()
    price: int = ask_for_price_gui()
    code: str = generate_code()
    today: str = datetime.today().strftime('%Y-%m-%d')
    generate_gift_card(price, code)
