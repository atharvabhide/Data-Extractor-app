import pdf2image
import pytesseract

# Convert the PDF to images
poppler_path = r"C:\Program Files\poppler-0.68.0\bin"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessarect_path = r""
images = pdf2image.convert_from_path(r'C:\Users\athar\OneDrive\Desktop\programming\projects\deeplogic ai assessment\files\pdf\sample1.pdf',
                                     poppler_path=poppler_path)

# Perform OCR on the images
text = []
for image in images:
    text.append(pytesseract.image_to_string(image))

# Create a new PDF with the OCR text
with open('output.pdf', 'w') as f:
    f.writelines(text)
