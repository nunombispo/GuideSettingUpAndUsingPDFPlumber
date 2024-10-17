import pdfplumber
from PIL import Image
import pytesseract

# Open the PDF file (scanned loan application)
with pdfplumber.open("Scanned Loan Application.pdf") as pdf:
    # Extract the first page (scanned document)
    first_page = pdf.pages[0]

    # Extract the page as an image
    image = first_page.to_image()

    # Save the image for OCR processing
    image.save("loan_application_page.png")

    # Load the saved image of the loan application
    image_path = "loan_application_page.png"
    ocr_text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(ocr_text)
