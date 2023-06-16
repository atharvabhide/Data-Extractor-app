from pdf2image import convert_from_path
from pytesseract import image_to_string
import pytesseract
from PIL import Image
import csv
import os 
from django.conf import settings

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
    data = None
    if file_path.endswith('.pdf'):
        data = get_text_from_any_pdf(file_path)
    elif file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.jpeg'):
        data = get_text_from_any_image(file_path)

    path = os.path.join(settings.MEDIA_ROOT, 'data')
    if not os.path.isdir(path):
        os.makedirs(path)
    csv_file_path = os.path.join(path, file_path.split("/")[-1] + ".csv")
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data.split("\n"):
            writer.writerow([line])
    return csv_file_path