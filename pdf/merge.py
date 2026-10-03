# from docx2pdf import convert
# from pypdf import PdfWriter
# merger = PdfWriter()
# # Make sure these paths match where your PDFs are stored
# files = ["pdf/file1.pdf", "pdf/file2.pdf", "pdf/file3.pdf"]
# for pdf in files:
#     merger.append(pdf)
# merger.write("pdf/merged-pdf.pdf")
# merger.close()


# Word to PDF Converter
# from docx2pdf import convert
# # Convert myFile.docx to file4.pdf
# convert("pdf/file4.pdf", "pdf/myFile.docx")
# print("Conversion complete! Check your pdf folder for file4.pdf.")


# PDF to word
# from pdf2docx import Converter
# pdf_file = "pdf/affidavit.pdf"
# docx_file = "pdf/AFFIDAVIT.docx"
# # Capital 'C' in Converter!
# cv = Converter(pdf_file)
# # Convert PDF to Word
# cv.convert(docx_file)
# # Close the converter
# cv.close()
# print("Conversion complete! file4.pdf is now saved as myFile.docx.")

import pymupdf  # Replaces 'fitz' to avoid warning
import pytesseract
from PIL import Image
import io
from docx import Document

# Point to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_path = "pdf/affidavit.pdf"
docx_path = "pdf/editable_scanned.docx"

doc_pdf = pymupdf.open(pdf_path)
doc_word = Document()

for page_num in range(len(doc_pdf)):
    page = doc_pdf[page_num]
    
    # Render PDF page to an image
    pix = page.get_pixmap(dpi=200)
    img_data = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_data))
    
    # Run OCR to extract text from image
    text = pytesseract.image_to_string(image)
    
    doc_word.add_heading(f'Page {page_num + 1}', level=2)
    doc_word.add_paragraph(text)

doc_word.save(docx_path)

print("Conversion complete! Check editable_scanned.docx in your pdf folder.")

