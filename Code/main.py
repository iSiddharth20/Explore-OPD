'''
Main Module
Talks to GUI, PreProcess, LLM, DB, Server
'''

# Import Necessary Modules
from preprocess import PreProcess
from gui import GUI

# Import Necessary Libraries
from dotenv import load_dotenv
from tkinter import filedialog


class ExploreOPD:
    def __init__(self):
        self.pdf_path = None
        self.preprocess = PreProcess()
        self.knowledge_base = self.preprocess.knowledge_base
        self.gui = GUI()

    def set_path(self, path=None):
        """ Updates the Path of PDF File """
        if path:
            self.pdf_path = path
        else:
            self.pdf_path = filedialog.askopenfilename()

    def update_knowledge_base(self):
        """ Updates Knowledge Base with Extracted Data """
        self.preprocess.extract_from_pdf(self.pdf_path)

    def app(self):
        button_get_file = self.gui.action_button("Select Source File", command=self.set_path)
        button_get_file.pack()

        button_proceed = self.gui.action_button("Update Knowledge_Base", command=self.update_knowledge_base)
        button_proceed.pack()


if __name__ == "__main__":
    load_dotenv()
    testrun = ExploreOPD()
    testrun.app()
    testrun.gui.start()
    print(f"""For the File Path: "{testrun.pdf_path}",\nThe Knowledge Base is:\n{testrun.knowledge_base}""")
