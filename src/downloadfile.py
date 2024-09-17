import os
import requests
import json

class PDFDownloader:
    def __init__(self, url_dict):
        self.url_dict = url_dict
        self.download_dir = "../DocumentCorpus"
        os.makedirs(self.download_dir, exist_ok=True)

    def download_pdfs(self):
        for filename, url in self.url_dict.items():
            pdf_path = os.path.join(self.download_dir, filename)
            if not os.path.exists(pdf_path):
                response = requests.get(url)
                if response.status_code == 200:
                    with open(pdf_path, "wb") as file:
                        file.write(response.content)
                    print(f"The file has been downloaded and saved as {pdf_path}")
                else:
                    print(f"Failed to download the file from {url}. Status code: {response.status_code}")
            else:
                print(f"File {pdf_path} exists.")

if __name__ == "__main__":
    json_input = '''
    {
        "fielding_dissertation.pdf": "https://ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf",
        "human_nutrition_text.pdf": "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"
    }
    '''
    url_dict = json.loads(json_input)
    downloader = PDFDownloader(url_dict)
    downloader.download_pdfs()