from PIL import Image, ImageDraw, ImageFont

import random 

import os 

import sys

POSSIBLE_AMOUNTS: list = [20, 50, 100]
CURRENT_PATH: str = os.path.dirname(__file__)
OUTPUT_FOLDER_PATH: str = os.path.join(CURRENT_PATH, "output")
OUTPUT_PATH: str = os.path.join(OUTPUT_FOLDER_PATH, "output.png")
ASSETS_FOLDER_PATH: str = os.path.join(CURRENT_PATH, "assets")
FONTS_FOLDER_PATH: str = os.path.join(ASSETS_FOLDER_PATH, "fonts")
FONT_courier: str = os.path.join(FONTS_FOLDER_PATH, "CourierPrime-Regular.ttf")
FONT_agrandir: str = os.path.join(FONTS_FOLDER_PATH, "Agrandir-GrandHeavy.otf")
TEMPLATE_FOLDER_PATH: str = os.path.join(ASSETS_FOLDER_PATH, "template")
TEMPLATE_PATH: str = os.path.join(TEMPLATE_FOLDER_PATH, "template.png")


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
    image_width, image_height = img.size
    draw = ImageDraw.Draw(img)
    
    amount_text: str = f"{amount}€"
    
    code_font = ImageFont.truetype(FONT_courier, 90)
    amount_font = ImageFont.truetype(FONT_agrandir, 250)
    
    _, _, code_width, code_height = draw.textbbox((0, 0), code, font=code_font)
    _, _, amount_width, amount_height = draw.textbbox((0, 0), amount_text, font=amount_font)
    
    draw.text(((image_width-code_width)/2, (image_height-code_height)/2), code, fill='black', font=code_font)
    draw.text(((image_width-amount_width)/2, 500), amount_text, fill='black', font=amount_font)

    img.save(OUTPUT_PATH)


if __name__ == "__main__": 
    if not os.path.exists(TEMPLATE_PATH):
        print("Template.png gibt es nicht. Programm wird beendet.")
        print(f"{TEMPLATE_PATH = }")
        sys.exit()

    generate_paths([OUTPUT_FOLDER_PATH])
    amount = 0
    # amount: int = get_amount(POSSIBLE_AMOUNTS)
    amount: int = 50 if not amount else amount
    code = get_code(10)
    
    generate_image()