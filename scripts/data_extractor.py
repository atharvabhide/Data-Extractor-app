from pdf2image import convert_from_path
from pytesseract import image_to_string
import pytesseract
import os 

POPPLER_PATH = r'C:\Program Files (x86)\poppler-23.05.0\Library\bin'
FILES_PATH = os.path.join(os.getcwd(), '../files')
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
    return convert_image_to_text(image_file)

for folder in os.listdir(FILES_PATH):
    for file in os.listdir(os.path.join(FILES_PATH, folder)):
        if file.endswith('.pdf'):
            print("File Name: ", file)
            print(get_text_from_any_pdf(os.path.join(FILES_PATH, folder, file)))
            print('*'*150)
        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            print("File Name: ", file)
            print(get_text_from_any_image(os.path.join(FILES_PATH, folder, file)))
            print('*'*150)