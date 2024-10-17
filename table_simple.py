# Import pdfplumber
import pdfplumber

# Open the PDF file (Bank of England Financials)
with pdfplumber.open("bank-of-england-financials.pdf") as pdf:
    # Access the first and only page of the PDF
    page = pdf.pages[0]

    # Extract tables from the page
    tables = page.extract_tables()

    # Iterate over tables and print them
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")
        for row in table:
            print(row)
        print("\\n")
