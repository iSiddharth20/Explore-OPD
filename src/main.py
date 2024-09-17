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

class DownloadURLs(BaseModel):
    urls: Dict[str, str]

@app.post("/downloadurls/")
def receive_download_urls(downloadurls: DownloadURLs):
    ''' Receive JSON containing PDF FileNames and Download URLs from Client '''
    try:
        downloader = PDFDownloader(downloadurls.urls)
        downloader.download_pdfs()
        return {"message": "Files downloaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/preprocesspdfs/")
def preprocess_downloaded_pdfs():
    ''' PreProcess PDF Files to Extract Data and Metadata (Filename, PageNumber) '''
    try:
        processor = PreProcess()
        download_dir = "../DocumentCorpus"
        if not os.path.exists(download_dir):
            raise HTTPException(status_code=404, detail="Download Directory Not Found")
        for filename in os.listdir(download_dir):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(download_dir, filename)
                processor.extract_from_pdf(pdf_path)
                # Append the knowledge_base object to the global list
                knowledge_bases.append(processor.knowledge_base)
        return {"message": "Files PreProcessed Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))