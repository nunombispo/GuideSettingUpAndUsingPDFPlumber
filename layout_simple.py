import pdfplumber

# Open the Chase Bank Statement PDF
with pdfplumber.open("Chase Freedom Bank Statement.pdf") as pdf:
    # Access the pages
    for page in pdf.pages:
        # Extract all text from the page with detailed positional data
        page_text = page.extract_text(layout=True)

        # Print the extracted text with preserved structure
        print(f"Page {page.page_number}:\n{page_text}\n")
