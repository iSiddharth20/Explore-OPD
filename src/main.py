'''
Main Module
'''

# Import Necessary Modules
from downloadfile import PDFDownloader
from preprocess import PreProcess

# Import Necessary Libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import os

app = FastAPI()
knowledge_bases = []

document_corpus_dir = "../DocumentCorpus"
os.makedirs(document_corpus_dir, exist_ok=True)

class DownloadURLs(BaseModel):
    urls: Dict[str, str]


@app.get("/download-pdf-from-url/")
def receive_download_urls(downloadurls: DownloadURLs):
    ''' Receive JSON containing PDF FileNames and Download URLs from Client '''
    try:
        downloader = PDFDownloader(document_corpus_dir, downloadurls.urls)
        downloader.download_pdfs()
        return {"message": "Files downloaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/preprocess-pdf/")
def preprocess_downloaded_pdfs():
    ''' PreProcess PDF Files to Extract Data and Metadata (Filename, PageNumber) '''
    try:
        processor = PreProcess()
        document_corpus_dir = "../DocumentCorpus"
        if not os.path.exists(document_corpus_dir):
            raise HTTPException(status_code=404, detail="Download Directory Not Found")
        for filename in os.listdir(document_corpus_dir):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(document_corpus_dir, filename)
                processor.extract_from_pdf(filename, pdf_path)
                # Append the knowledge_base object to the global list
                knowledge_bases.append(processor.knowledge_base)
        return {"message": "Files PreProcessed Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

