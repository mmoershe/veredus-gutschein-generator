from modules.CONST import TEMPLATE_IMAGE_DIR, FONT_courier, FONT_agrandir, FONT_ubuntu, FONT_geist, OUTPUT_FILE_DIR

from PIL import Image, ImageDraw, ImageFont


def generate_gift_card(amount: int, code: str, date: str) -> None: 
    img = Image.open(TEMPLATE_IMAGE_DIR)
    image_width, image_height = img.size
    draw = ImageDraw.Draw(img)
    
    amount_text: str = f"{amount}€"
    
    code_font = ImageFont.truetype(FONT_geist, 37)
    date_font = ImageFont.truetype(FONT_geist, 20)
    amount_font = ImageFont.truetype(FONT_agrandir, 150)
    
    _, _, code_width, code_height = draw.textbbox((0, 0), code, font=code_font)
    _, _, date_width, date_height = draw.textbbox((0, 0), code, font=date_font)
    _, _, amount_width, amount_height = draw.textbbox((0, 0), amount_text, font=amount_font)
    
    draw.text(((image_width-code_width)/2, 965), code, fill='black', font=code_font)
    draw.text(((image_width-date_width)/2, 1130), date, fill='black', font=date_font)
    draw.text(((image_width-amount_width)/2, 600), amount_text, fill='black', font=amount_font)

    img.save(OUTPUT_FILE_DIR, "PDF", resolution=100.0)
