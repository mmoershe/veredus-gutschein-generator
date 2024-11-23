import tkinter as tk
from tkinter import simpledialog

def ask_for_price_gui() -> int:
    # Initialize the main application window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Create the dialog to get user input
    price_value = None
    while True:
        try:
            price_value = simpledialog.askinteger("Input", "Gib den Wert des Geschenkgutscheins als Zahl ein:")
            if price_value is not None:  # Ensure the user didn't cancel
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid integer.")

    # Destroy the root window after getting the input
    root.destroy()
    return price_value

