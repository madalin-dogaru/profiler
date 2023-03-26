import argparse
import requests
import json
import socket
import sys
import os
import re
from termcolor import colored

class ColoredArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (colored(self.prog, "red"), colored(message, "red")))

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

        return urls

class IPInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    def get_ip_info(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = json.loads(response.content)

        if data["status"] == "success":
            result = f"{ip},{data['country']},{data['regionName']},{data['city']}"
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
                    result = IPInfo(self.output_handle).get_ip_info(ip)
                    if result:
                        print(result)
                        if self.output_handle:
                            self.output_handle.write(result + "\n")
                            self.output_handle.flush()

def parse_arguments():
    parser = ColoredArgumentParser(description='Get IP information and save to a file.')
    parser.add_argument('-iplist', help='Path to the file containing the list of IP addresses.')
    parser.add_argument('-ip', help='A single IP address to get information.')
    parser.add_argument('-d', '--domain', help='A single domain name to get information.')
    parser.add_argument('-dlist', help='Path to the file containing the list of domain names.')
    parser.add_argument('-url', help='Path to the folder containing files to scan for URLs.')
    parser.add_argument('-o', '--output-file', help='Path to the output file.')
    return parser.parse_args()

def process_url_scan(folder_path, output_handle):
    scanner = URLScanner(folder_path)
    urls = scanner.scan_folder()

    for url in urls:
        print(url)
        if output_handle:
            output_handle.write(url + "\n")
            output_handle.flush()

def main():
    args = parse_arguments()
    input_file = args.iplist
    single_ip = args.ip
    domain = args.domain
    domain_list = args.dlist
    folder_path = args.url
    output_file = args.output_file

    output_handle = open(output_file, "w") if output_file else None

    ip_info = IPInfo(output_handle)
    domain_info = DomainInfo(output_handle)

    if input_file:
        ip_info.process_ip_list(input_file)
    elif domain_list:
        domain_info.process_domain_list(domain_list)
    elif single_ip:
        result = ip_info.get_ip_info(single_ip)
        if result:
            print(result)
            if output_handle:
                output_handle.write(result + "\n")
                output_handle.flush()
    elif domain:
        ip = domain_info.get_domain_ip(domain)
        if ip:
            result = ip_info.get_ip_info(ip)
            if result:
                print(result)
                if output_handle:
                    output_handle.write(result + "\n")
                    output_handle.flush()
    elif folder_path:
        process_url_scan(folder_path, output_handle)
    else:
        print(colored("Please provide either a single IP (-ip), a domain (-d), a list of IPs (-iplist), a list of domains (-dlist), or a folder to scan for URLs (-url).", "yellow"))

    if output_handle:
        output_handle.close()

if __name__ == '__main__':
    main()
