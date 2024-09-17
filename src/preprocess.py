'''
Pre-Processing the Documents and Create Chunks
Talks to Main, GUI, LLM
'''

# Import Necessary Libraries
import os
import pymupdf as fitz


class PreProcess:
    def __init__(self):
        self.knowledge_base = []

    def append_to_knowledge_base(self, filename, page_number, text=None):
        """ Add Extracted & Formatted Data to Knowledge Base """
        self.knowledge_base.append({"filename": filename,
                                    "page_number": page_number+1,
                                    "text": text})

    def format_text(self, text):
        """ Format the Extracted Text """
        text = text.replace('\n', ' ').strip()
        sentences = text.split('. ')
        sentences = [sentence.strip() for sentence in sentences]
        return sentences

    def extract_from_pdf(self, doc_path):
        """ Extract Contents from PDF and Store it with Metadata (Filename, Page Number, Content) """
        doc = fitz.open(doc_path, filetype="pdf")
        filename = os.path.basename(doc_path)
        for page_number, page in enumerate(doc):
            # Extract Text from the Page
            text = page.get_text()
            text = self.format_text(text)
            self.append_to_knowledge_base(filename, page_number, text=text)


if __name__ == "__main__":
    testrun = PreProcess()
    pdf_path = r"../DocumentCorpus/fielding_dissertation.pdf"
    testrun.extract_from_pdf(pdf_path)
    print(f"""For the File Path: "{pdf_path}",\nSlice of Knowledge Base is:\n{testrun.knowledge_base[0]}""")
