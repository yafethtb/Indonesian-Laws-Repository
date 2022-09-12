import pytesseract
import fitz
from PIL import Image
from sys import argv

# argv[1] = PDF file name.
# argv[2] = TXT file name.

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe' 

def pdf_extractor(pdf_file):
    '''Open and extract'''
    pdf_open  = fitz.open(pdf_file)

    for page_index in range(len(pdf_open)):
        page = pdf_open[page_index]
        image_info = page.get_pixmap().pil_save(f"{page_index}.png", optimize = True, dpi = (600, 600))  
        print(f'{page_index}.png is saved')

    image_list = [f'{i}.png' for i in range(len(pdf_open))]

    image_text = []
    print("Tesseract process...")
    
    for image in image_list:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        image_text.append(text)
        print(f'{image} text is appended.')
    
    return ' '.join(image_text)

if __name__ == "__main__":
    with open(argv[2], 'w') as uu:
        uu.write(pdf_extractor(argv[1]))

print('Process done.')