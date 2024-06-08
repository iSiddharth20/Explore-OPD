'''
Pre-Processing the Documents and Create Chunks
Talks to Main, GUI, LLM
'''

# Import Necessary Libraries
import os
import pymupdf as fitz


# Define Class for this Module
class PreProcess:
    def __init__(self):
        pass

    # Function to Format the Extracted Text
    def format_text(self, text):
        text = text.replace("\n", " ").strip()
        text = text.replace("\t", " ").strip()
        return text


    def extract_from_pdf(self, doc_path):
        doc = fitz.open(doc_path, filetype="pdf")
        doc_text_with_metadata = []
        filename = os.path.basename(doc_path)
        for page_number, page in enumerate(doc):
            # Extract and Process Text on the Page
            text = page.get_text()
            text = self.format_text(text)
            # Store the Extracted Data
            doc_text_with_metadata.append({"filename": filename,
                                           "page_number": page_number+1,
                                           "text": text})
        return doc_text_with_metadata


if __name__ == "__main__":
    testrun = PreProcess()
    pdf_path = r"../SampleDocuments/SampleDoc.pdf"
    doc_data = testrun.extract_from_pdf(pdf_path)
    print(doc_data)

