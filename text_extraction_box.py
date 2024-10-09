# Import pdfplumber
import pdfplumber

# Open the PDF file (Chase Bank Statement)
with pdfplumber.open("Chase Freedom Bank Statement.pdf") as pdf:
    # Get the second page of the PDF
    second_page = pdf.pages[1]

    # Define a bounding box for the transactions area (x0, y0, x1, y1)
    bbox = (50, 100, 550, 550)

    # Extract text from the defined region
    transactions_text = second_page.within_bbox(bbox).extract_text()

    # Print the extracted transactions text
    print(transactions_text)
