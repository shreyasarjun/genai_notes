import os
import glob
import re
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import tabula

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Input file
PDF_FILE_PATH = r"C:\Users\ShreyasBilikereShant\Downloads\test2.pdf"

# Output data
EXTRACTION_RESULTS = {
    "Tabular_Data": {},
    "Text_Data": "",
    "Image_Text_Data": "",
    "Extracted_Images": [],
}

# Patterns for image text processing
PATTERN = r".+(_).+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"


def extract_normal_text_from_pdf(pdf_file):
    """
    Extract normal text data from the PDF using PyMuPDF.
    """
    try:
        doc = fitz.open(pdf_file)
        text = ""
        for page in doc:
            text += page.get_text()  # Extract text from each page
        EXTRACTION_RESULTS["Text_Data"] = text.strip()
    except Exception as e:
        print(f"Error extracting normal text: {e}")


def extract_tabular_data_from_pdf(pdf_file):
    """
    Extract tabular data from the PDF using Tabula with fallback to PyMuPDF if needed.
    """
    try:
        # Extract tables using Tabula
        tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
        if not tables or len(tables) == 0:
            print("No tables found using Tabula. Fallback to text-based extraction.")
        else:
            tabular_data = []
            for table in tables:
                tabular_data.append(table.to_dict(orient="records"))  # Convert DataFrame to dictionary
            EXTRACTION_RESULTS["Tabular_Data"] = tabular_data
    except Exception as e:
        print(f"Error extracting tabular data with Tabula: {e}")


def extract_images_from_pdf(pdf_file):
    """
    Extract images from the PDF and save them as PNG files.
    """
    try:
        output_dir = "./images/"
        os.makedirs(output_dir, exist_ok=True)

        # Clear existing images in the output directory
        for img_file in glob.glob(f"{output_dir}*"):
            os.remove(img_file)

        doc = fitz.open(pdf_file)
        for page_index in range(len(doc)):
            for img_index, img in enumerate(doc[page_index].get_images(full=True)):
                xref = img[0]
                base_image = fitz.Pixmap(doc, xref)
                img_file_path = f"{output_dir}page_{page_index+1}_img_{img_index+1}.png"

                if base_image.n < 5:  # GRAY or RGB
                    base_image.save(img_file_path)
                else:  # CMYK: Convert to RGB
                    rgb_image = fitz.Pixmap(fitz.csRGB, base_image)
                    rgb_image.save(img_file_path)
                    rgb_image = None

                EXTRACTION_RESULTS["Extracted_Images"].append(img_file_path)

    except Exception as e:
        print(f"Error extracting images: {e}")


def extract_text_from_images():
    """
    Use Tesseract OCR to extract text from extracted images.
    """
    try:
        extracted_text = []
        for img_path in EXTRACTION_RESULTS["Extracted_Images"]:
            text = pytesseract.image_to_string(Image.open(img_path), lang="eng").strip()
            extracted_text.append(text)

            # Optionally process with regex
            match = re.search(PATTERN, text)
            if match:
                print(f"Regex Match: {match.group()}")

        EXTRACTION_RESULTS["Image_Text_Data"] = " ".join(extracted_text)

    except Exception as e:
        print(f"Error extracting text from images: {e}")


if __name__ == '__main__':
    # Step 1: Extract normal text
    extract_normal_text_from_pdf(PDF_FILE_PATH)

    # Step 2: Extract tabular data
    extract_tabular_data_from_pdf(PDF_FILE_PATH)

    # Step 3: Extract images
    extract_images_from_pdf(PDF_FILE_PATH)

    # Step 4: Extract text from images
    extract_text_from_images()

    # Final output
    print("\nExtraction Results:")
    print(EXTRACTION_RESULTS)
