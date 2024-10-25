import nltk
import PyPDF2
from fpdf import FPDF

# Extract text from PDF function (as done previously)
def extract_text_from_pdf(pdf_path="C:/Users/TANU/Desktop/major/chatbot.pdf"):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to save tokenized text into a new PDF file
def save_tokenized_data_to_pdf(tokens, output_pdf_path="tokenized_output.pdf"):
    # Create a PDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add the tokenized words to the PDF, while handling unsupported characters
    for token in tokens:
        # Encode the token to 'latin-1' and replace any unsupported characters
        token = token.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=token, ln=True, align='L')  # Add each token as a new line

    # Output the PDF
    pdf.output(output_pdf_path)

# Main process
pdf_path = "C:/Users/TANU/Desktop/major/chatbot.pdf"  # Path to the PDF you want to tokenize

# Step 1: Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Step 2: Tokenize the extracted text using nltk
nltk.download('punkt')
tokens = nltk.word_tokenize(pdf_text)

# Step 3: Save the tokenized data into a new PDF
output_pdf_path = "C:/Users/TANU/Desktop/tokenized_output.pdf"
save_tokenized_data_to_pdf(tokens, output_pdf_path)

print(f"Tokenized data saved to: {output_pdf_path}")
