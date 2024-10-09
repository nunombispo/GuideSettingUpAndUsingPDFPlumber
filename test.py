# Import pdfplumber
import pdfplumber

# Open the PDF file
with pdfplumber.open("Chase Freedom Bank Statement.pdf") as pdf:
    # Access the first page of the PDF
    first_page = pdf.pages[0]

    # Extract the text from the first page
    text = first_page.extract_text()

    # Print the extracted text
    print(text)
