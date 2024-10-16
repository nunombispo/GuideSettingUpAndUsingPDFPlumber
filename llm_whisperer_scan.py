from unstract.llmwhisperer.client import LLMWhispererClient

# Initialize the client with your API key
client = LLMWhispererClient(base_url="https://llmwhisperer-api.unstract.com/v1",
                            api_key='<your-api-key>',
                            api_timeout=300)

# Extract tables from the PDF
result = client.whisper(file_path="Scanned Loan Application.pdf", output_mode="line-printer")
extracted_text = result["extracted_text"]

# Print the extracted text
print(extracted_text)
