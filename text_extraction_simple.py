# Import pdfplumber
import pdfplumber

# Open the PDF file (Chase Bank Statement)
with pdfplumber.open("Chase Freedom Bank Statement.pdf") as pdf:
    # Iterate over each page in the PDF
    for page in pdf.pages:
        # Extract the text from the page
        page_text = page.extract_text()
        # Print the extracted text
        print(f"Page {page.page_number}:\n{page_text}\n")
