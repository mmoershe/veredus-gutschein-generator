from modules.setup import setup 
from modules.code import generate_code
from modules.tkinter import ask_for_price_gui
from modules.generation import generate_gift_card


if __name__ == "__main__": 
    setup()
    price: int = ask_for_price_gui()
    price: int = 33
    code: str = generate_code()
    generate_gift_card(price, code)
