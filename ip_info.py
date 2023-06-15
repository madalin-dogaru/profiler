"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

import requests
import json
from termcolor import colored

class IPInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    def get_ip_info(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = json.loads(response.content)

        if data["status"] == "success":
            green_ip = colored(ip, "green")
            cyan_country = colored(data['country'], "light_cyan")
            white_city = colored(data['city'], "white")
            dark_region = colored(data['regionName'], "dark_grey")

            result = f"{green_ip},{cyan_country},{white_city},{dark_region}"
            return result
        else:
            print(colored(f"Failed to retrieve information for IP: {ip}", "red"))
            return None

    def process_ip_list(self, input_file):
        with open(input_file, "r") as ip_file:
            for line in ip_file:
                ip = line.strip()
                result = self.get_ip_info(ip)
                if result:
                    print(result)
                    if self.output_handle:
                        self.output_handle.write(result + "\n")
                        self.output_handle.flush()
