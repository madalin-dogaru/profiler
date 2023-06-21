"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: GPLv3
Description: A Red Teaming tool focused on profiling the target.
"""

import requests
import json

class BinaryEdgeAPI:
    base_url = 'https://api.binaryedge.io/v2'

    def __init__(self, token: str):
        self.token = token
        self.headers = {'X-Key': self.token,}

    def get_host_details(self, target: str) -> dict:
        response = requests.get(f'{self.base_url}/query/ip/{target}', headers=self.headers)
        return response.json()

    def format_data(self, data: dict) -> str:
        formatted_data = json.dumps(data, indent=4, sort_keys=True)
        return formatted_data
