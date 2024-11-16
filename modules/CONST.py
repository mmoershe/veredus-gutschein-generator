import os 


###############
# DIRECTORIES #
###############
MODULES_DIR: str = os.path.dirname(__file__)
BASE_DIR: str = os.path.dirname(MODULES_DIR)
ASSETS_DIR: str = os.path.join(BASE_DIR, "assets")
DATA_DIR: str = os.path.join(ASSETS_DIR, "DATA.json")
TEMPLATE_DIR: str = os.path.join(ASSETS_DIR, "template")
TEMPLATE_IMAGE_DIR: str = os.path.join(TEMPLATE_DIR, "template.png")
FONTS_DIR: str = os.path.join(ASSETS_DIR, "fonts")
FONT_courier: str = os.path.join(FONTS_DIR, "CourierPrime-Regular.ttf")
FONT_agrandir: str = os.path.join(FONTS_DIR, "Agrandir-GrandHeavy.otf")
OUTPUT_DIR: str = os.path.join(BASE_DIR, "output")
OUTPUT_FILE_DIR: str = os.path.join(OUTPUT_DIR, "gutschein.pdf")
