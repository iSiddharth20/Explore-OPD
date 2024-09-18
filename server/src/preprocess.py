'''
Extracts Data (Text Paragraphs) and Metadata (FileName, PageNumber) from PDF Documents
'''

# Import Necessary Libraries
import os
import pymupdf as fitz
from spacy.lang.en import English


class PreProcess:
    def __init__(self):
        self.knowledge_base = []

    def append_to_knowledge_base(self, filename, page_number, text=None):
        """ Add Extracted & Formatted Data to Knowledge Base of this Document"""
        self.knowledge_base.append({"filename": filename,
                                    "page_number": page_number+1,
                                    "text": text})

    def format_text(self, text):
        """ Split the Extracted Text into Sentences using spaCy """
        nlp = English()
        nlp.add_pipe("sentencizer")
        text = text.replace('\n', ' ').strip()
        sentences = list(nlp(text).sents)
        sentences = [str(sntc) for sntc in sentences]
        return sentences

    def extract_from_pdf(self, filename, doc_path):
        """ Extract Contents from PDF and Store it with Metadata (Filename, Page Number, Content) """
        doc = fitz.open(doc_path, filetype="pdf")
        for page_number, page in enumerate(doc):
            text = page.get_text()
            text = self.format_text(text)
            self.append_to_knowledge_base(filename, page_number, text=text)


if __name__ == "__main__":
    testrun = PreProcess()
    pdf_path = r"../DocumentCorpus/fielding_dissertation.pdf"
    filename = "fielding_dissertation"
    testrun.extract_from_pdf(filename, pdf_path)
    print(f"""For the File Path: "{pdf_path}",\nSlice of Knowledge Base is:\n{testrun.knowledge_base[10]}""")
