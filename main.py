from PIL import Image, ImageDraw

import random 

import os 

import sys

POSSIBLE_AMOUNTS: list = [20, 50, 100]
CURRENT_PATH: str = os.path.dirname(__file__)
OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "output")
TEMPLATE_PATH: str = os.path.join(CURRENT_PATH, "template", "template.png")


def generate_paths(paths: list) -> None: 
    for path in paths: 
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created Path: {path}")


def get_amount(amounts: list) -> int: 
    while True: 
        try:
            for i, amount in enumerate(amounts):
                print(f"{i}\t{amount}€")
            chosen_amount: int = amounts[int(input(f"Für welchen Geldbetrag soll ein Geschenkgutschein generiert werden?\t"))]
        except ValueError:
            print("\nBitte gib eine ganze Zahl ein!")    
        except IndexError:
            print(f"\nBitte gib eine Zahl von 0 bis {len(amounts)-1} ein!")    
        else: 
            print(f"Ein Geschenkgutschein für {chosen_amount}€ wird erstellt...\n")
            return int(chosen_amount)
    
    
def get_code(code_length: int=8) -> str:
    code_content: list = ["ABCDEFGHJKLMNPQRSTUVWXYZ23456789"]
    return "".join([random.choice(code_content[0]) for i in range(code_length)])


def generate_image() -> None: 
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)
    
    draw.text((100, 100), code, fill='black')
    
    img.save(os.path.join(OUTPUT_PATH, "output.png"))


if __name__ == "__main__": 
    if not os.path.exists(TEMPLATE_PATH):
        print("Template.png gibt es nicht. Programm wird beendet.")
        sys.exit()

    generate_paths([OUTPUT_PATH])
    amount = get_amount(POSSIBLE_AMOUNTS)
    code = get_code(10)
    
    generate_image()