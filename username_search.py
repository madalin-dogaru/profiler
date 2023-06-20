"""
Title: profiler
Author: Mădălin Dogaru
Contributor: Genadi Shamugia
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: GPLv3
Description: A Red Teaming tool focused on profiling the target.
"""

import argparse
import concurrent.futures
import requests
import json

class UsernameProfiler:
    def __init__(self, username):
        self.username = username
        self.url = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"

    def make_request(self, url, account):
        url = url.replace("{account}", account)
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return 0, 0
        return response.status_code, response.text

    def process_site(self, site):
        name = site["name"]
        uri_check = site["uri_check"].replace("{account}", self.username)
        cat = site["cat"]

        status_code, response_text = self.make_request(uri_check, self.username)

        if status_code == 200:
            return name, cat, uri_check
        else:
            return None

    def run(self):
        response = requests.get(self.url)
        data = json.loads(response.text)

        sites = data["sites"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(self.process_site, site) for site in sites]
            try:
                for future in concurrent.futures.as_completed(results):
                    result = future.result()
                    if result:
                        name, cat, uri_check = result
                        print("Name:", name)
                        print("Category:", cat)
                        print("URI Check:", uri_check)
                        print()
            except KeyboardInterrupt:
                print("Program interrupted. Exiting...")