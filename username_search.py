"""
Title: profiler
Author: Mădălin Dogaru
Contributor: Genadi Shamugia
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: GPLv3
Used WhatsMyName's source file: https://github.com/WebBreacher/WhatsMyName/blob/main/wmn-data.json
Description: A Red Teaming tool focused on profiling the target.
"""

import requests
import json
import concurrent.futures
from termcolor import colored
import os

class UsernameProfiler:
    def __init__(self, username, verbose=False):
        self.username = username
        self.verbose = verbose

    @staticmethod
    def load_websites():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, 'assets')
        with open(os.path.join(assets_dir, 'websites.json')) as file:
            data = json.load(file)
        return data["sites"]

    def check_username(self, username, site):
        uri = site['uri_check'].replace('{account}', username)
        try:
            response = requests.get(uri, timeout=5) # Add timeout to prevent hanging requests

            if site['e_code'] == response.status_code:
                if site['e_string'] in response.text:
                    print(f"{site['name']}:{uri}")
        except requests.exceptions.RequestException as e:
            if self.verbose:
                print(f"An error occurred when checking {site['name']}: {str(e)}")
        except requests.exceptions.SSLError as e:
            if self.verbose:
                print(f"An SSL error occurred when checking {site['name']}: {str(e)}")
        except Exception as e:
            if self.verbose:
                print(f"An unexpected error occurred when checking {site['name']}: {str(e)}")

    def run(self, verbose=False):
        self.verbose = verbose
        websites = self.load_websites()
        executor = concurrent.futures.ThreadPoolExecutor()

        try:
            list(executor.map(lambda site: self.check_username(self.username, site), websites))
        except KeyboardInterrupt:
            executor.shutdown(wait=False)
            print(colored(f"Program interrupted. Exiting...", 'red'))
        finally:
            executor.shutdown(wait=True)
