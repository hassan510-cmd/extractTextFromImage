import pytesseract as converter
from PIL import Image
converter.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
target = Image.open("Ann.png")
text = converter.image_to_string(target)
print(text)
