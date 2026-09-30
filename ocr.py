import pytesseract
from PIL import Image


def extract_text(image: Image.Image) -> str:
    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )

    return text.strip()
