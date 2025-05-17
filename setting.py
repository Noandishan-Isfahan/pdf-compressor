import sys
from pathlib import Path

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    ROOT_DIR = Path(sys._MEIPASS)  # type: ignore # For PyInstaller
else:
    ROOT_DIR = Path(__file__).parent
FONT_DIR = ROOT_DIR / "img" / "fonts"
FONT_NAMES = ["Vazirmatn-Regular.ttf"]
FONTS = [str(FONT_DIR / font) for font in FONT_NAMES]

TEMP_FOLDER = ROOT_DIR / "temp"

MAIN_ICON = ROOT_DIR / "img" / "default_images" / "nhs-logo.ico"
MAIN_LOGO = ROOT_DIR / "img" / "default_images" / "nhs-logo.png"


DEFUALT_COLOR_IMAGE_RES = 125
DEFUALT_GRAY_IMAGE_RES = 115
DEFUALT_MONO_IMAGE_RES = 150
