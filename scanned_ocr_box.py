import pdfplumber
import pytesseract

# Open the PDF file (scanned loan application)
with pdfplumber.open("Scanned Loan Application.pdf") as pdf:
    # Extract the first page (scanned document)
    first_page = pdf.pages[0]

    # Define a bounding box around the form field (x0, y0, x1, y1)
    bbox = (25, 150, 250, 200)  # Coordinates for the name field

    # Crop the image to focus on the form field
    cropped_image = first_page.within_bbox(bbox).to_image()
    cropped_image.save("cropped_name_field.png")  # For debugging purposes

    # Apply OCR on the cropped image
    field_text = pytesseract.image_to_string(cropped_image.original)
    print("Extracted Form Field Data:\n", field_text)
