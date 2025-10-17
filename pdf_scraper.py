import requests
from b4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
from pyPDF2 import PdfMerger
import os
# from pathlib import Path

def fetch_pdf_links(url):
    print(f"🕵🏻 Looking for PDFs at: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        pdf_links = []
        for link in soup.find_all('a'):
            href = link.get('href')

            if href and '.pdf' in href.lower(): #checks if it's a pdf
                full_url = urljoin(url, href)
                pdf_links.append(full_url)
                print(f"🥸 Found PDF: {full_url}")
        return pdf_links
    
    except Exception as e:
        print(f"🙅🏻‍♂️ Error finding PDFs: {e}")
        return
    