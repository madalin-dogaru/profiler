"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

import os
import re

class URLScanner:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_urls(self, text):
        return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    def scan_folder(self):
        urls = []

        for root, _, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    extracted_urls = self.extract_urls(content)
                    urls.extend(extracted_urls)

        return list(set(urls))  # Here we convert the list of URLs to a set (which removes duplicates) and then back to a list
