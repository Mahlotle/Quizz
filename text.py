import PyPDF2
import random

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            # Extract text and split into lines
            page_text = page.extract_text().splitlines()
            # Iterate through lines, keeping only those starting with a letter
            text += "\n".join([line for line in page_text if line and line[0].isalpha()])
    return text

def select_text_from_pdf(pdf_path, batch_size=10000, num_batches=2):
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Calculate the total number of words in the preprocessed text
    total_words = len(pdf_text)

    # Check if the batch size and number of batches exceed the total words
    if batch_size * num_batches > total_words:
        # Adjust the batch size and number of batches based on the document length
        batch_size = total_words // num_batches
        if batch_size == 0:
            batch_size = total_words  # If the PDF is too short, use all the text
            num_batches = 1

    # Randomly select starting indices for the batches
    selected_start_indices = random.sample(range(total_words - batch_size), num_batches)

    # Initialize the selected text
    selected_text = ""

    # Extract text for each selected batch and concatenate
    for start_index in selected_start_indices:
        end_index = start_index + batch_size
        selected_text += pdf_text[start_index:end_index]

    return selected_text
