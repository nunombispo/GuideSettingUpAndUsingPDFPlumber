import pdfplumber

# Open the Chase Bank Statement PDF
with pdfplumber.open("Chase Freedom Bank Statement.pdf") as pdf:
    # Access the first page
    first_page = pdf.pages[0]

    # Extract layout elements
    page_layout = first_page.extract_words()

    # Print each word with its positional data
    for word in page_layout:
        print(word)
