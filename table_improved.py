# Import pdfplumber
import pdfplumber

# Open the PDF file (Bank of England Financials)
with pdfplumber.open("bank-of-england-financials.pdf") as pdf:
    # Access the first and only page of the PDF
    page = pdf.pages[0]

    # Use improved table extraction with edge detection
    table = page.extract_table({
        "vertical_strategy": "lines",  # Looks for vertical lines separating columns
        "horizontal_strategy": "text",  # Uses text positioning for rows
        "intersection_tolerance": 5,  # Adjusts for minor misalignment
    })

    # Print the extracted table
    for row in table:
        print(row)