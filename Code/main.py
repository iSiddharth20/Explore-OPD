'''
Main Module
Talks to GUI, PreProcess, LLM, DB, Server
'''

# Import Necessary Modules
from preprocess import PreProcess


class ExploreOPD:
    def __init__(self):
        self.pdf_path = None
        self.preprocess = PreProcess()

    def get_path(self, path):
        self.pdf_path = path

    def update_knowledge_base(self):
        self.preprocess.extract_from_pdf(self.pdf_path)


if __name__ == "__main__":
    testrun = ExploreOPD()
    pdf_path = r"../SampleDocuments/SampleDoc.pdf"
    testrun.get_path(pdf_path)
    testrun.update_knowledge_base()
    print(f"""For the File Path: "{pdf_path}",\nThe Knowledge Base is:\n{testrun.preprocess.knowledge_base}""")
