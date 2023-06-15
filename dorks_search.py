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
from serpapi import GoogleSearch

def read_dorks_from_file(file_path):
    with open(file_path, 'r') as f:
        dorks = [line.strip() for line in f]
    return dorks

def google_dork(domain, dorks_file):
    if not os.path.isfile(dorks_file):
        print(f"\033[91mError: The file '{dorks_file}' does not exist. Please provide a valid file path.\033[0m")
        return
    dorks = read_dorks_from_file(dorks_file)

    # Replace "your_api_key" with your SerpApi key
    api_key = "your_api_key"

    for dork in dorks:
        dork_with_site = f"site:{domain} {dork}"
        params = {
            "q": dork_with_site,
            "api_key": "your_api_key",
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        found_links = set()

        if 'organic_results' in results:
            for link in results['organic_results']:
                url = link['link']
                if domain in url:
                    found_links.add(url)

        if found_links:
            print(f"\033[32m+++ RESULTS: {dork_with_site}\033[0m")
            for link in found_links:
                print(link)
            print()
        else:
            print(f"\033[91m--- NO RESULTS FOR: {dork_with_site}\033[0m\n")

