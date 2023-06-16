from pdf2image import convert_from_path
from pytesseract import image_to_string
import pytesseract
import os 
from PIL import Image

POPPLER_PATH = r'C:\Program Files (x86)\poppler-23.05.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file, poppler_path=POPPLER_PATH)

def convert_image_to_text(file):
    text = image_to_string(file)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)
    return final_text

def get_text_from_any_image(image_file):
    image = Image.open(image_file)
    return convert_image_to_text(image)

def extract_data(file_path):
    data = {}
    if file_path.endswith('.pdf'):
        data[file_path] = get_text_from_any_pdf(f"../media/files/{file_path}")
    elif file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.jpeg'):
        data[file_path] = get_text_from_any_image(f"../media/files/{file_path}")
    with open(f'../media/data/{file_path}.csv', 'w') as out:
        out.write(data[file_path])