import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pdfplumber
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

def preprocess_image(image):
    """
    Preprocess the image for better OCR performance.
    """
    # Convert image to grayscale
    image = image.convert("L")
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    # Apply slight blur to reduce noise
    image = image.filter(ImageFilter.MedianFilter())
    return image

def extract_text_from_pdf(file_path):
    """
    Extract text, tables, and images from a PDF file.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # Extract text from the page
            if page.extract_text():
                text += page.extract_text()
            
            # Extract tables
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    cleaned_row = [str(cell) if cell is not None else "" for cell in row]
                    text += "\t".join(cleaned_row) + "\n"
            
            # Extract images
            for image in page.images:
                if "object_id" in image:
                    try:
                        # Use xref to locate the image stream
                        xref = image["object_id"]
                        image_stream = pdf.streams.get(xref)
                        if image_stream:
                            image_bytes = image_stream.get_data()
                            with BytesIO(image_bytes) as img_stream:
                                base_image = Image.open(img_stream)
                                # Preprocess the image
                                processed_image = preprocess_image(base_image)
                                # Save for debugging (optional)
                                processed_image.save(f"debug_image_page_{page.page_number}.png")
                                # Extract text from the image using pytesseract
                                extracted_text = pytesseract.image_to_string(processed_image, lang="eng")
                                text += extracted_text
                    except Exception as e:
                        print(f"Error processing image on page {page.page_number}: {e}")
                else:
                    pass
                    #print(f"Skipping image on page {page.page_number}: missing 'object_id'")
    return text

def load_pdfs(folder_path):
    """
    Load and extract text from all PDFs in a folder.
    """
    import os
    pdf_texts = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            full_path = os.path.join(folder_path, file_name)
            pdf_texts[file_name] = extract_text_from_pdf(full_path)
    return pdf_texts

# Example usage
pdf_texts = load_pdfs("./data/pdfs")
print(pdf_texts)
