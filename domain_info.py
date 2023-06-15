"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

import socket
from termcolor import colored
from ip_info import IPInfo

class DomainInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    def get_domain_ip(self, domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.gaierror:
            print(colored(f"Failed to resolve the domain: {domain}", "red"))
            return None

    def process_domain_list(self, domain_list):
        with open(domain_list, "r") as domain_file:
            for line in domain_file:
                domain = line.strip()
                ip = self.get_domain_ip(domain)
                if ip:
                    ip_info = IPInfo(self.output_handle)
                    result = ip_info.get_ip_info(ip)
                    if result:
                        print(result)
                        if self.output_handle:
                            self.output_handle.write(result + "\n")
                            self.output_handle.flush()
