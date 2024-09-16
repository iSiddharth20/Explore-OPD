'''
Main Module
'''

# Import Necessary Modules
from downloadfile import PDFDownloader

# Import Necessary Libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

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