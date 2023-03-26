import argparse
import requests
import json
import socket
import sys
import os
import re
from termcolor import colored

# Custom ArgumentParser class with colored error messages
class ColoredArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (colored(self.prog, "red"), colored(message, "red")))

# Class for generating various email formats from firstname and lastname pairs
class EmailGenerator:
    def __init__(self, firstname_lastname_list, domain):
        self.firstname_lastname_list = firstname_lastname_list
        self.domain = domain

    # Generate a list of possible email formats for each user
    def generate_emails(self, users):
        emails = []
        for firstname, lastname in users:
            emails.append(f'{firstname}.{lastname}@{self.domain}')
            emails.append(f'{lastname}.{firstname}@{self.domain}')
            emails.append(f'{firstname}_{lastname}@{self.domain}')
            emails.append(f'{lastname}_{firstname}@{self.domain}')
            emails.append(f'{firstname}-{lastname}@{self.domain}')
            emails.append(f'{lastname}-{firstname}@{self.domain}')
            emails.append(f'{firstname}{lastname}@{self.domain}')
            emails.append(f'{lastname}{firstname}@{self.domain}')
            emails.append(f'{firstname[0]}{lastname}@{self.domain}')
            emails.append(f'{lastname[0]}{firstname}@{self.domain}')
            emails.append(f'{firstname}@{self.domain}')
            emails.append(f'{lastname}@{self.domain}')
        return emails
    
    # Process the list of firstnames and lastnames, and generate emails
    def process_name_list(self, output_handle):
        users = []
        with open(self.firstname_lastname_list, "r") as name_file:
            for line in name_file:
                firstname, lastname = line.strip().split()
                users.append((firstname, lastname))

        emails = self.generate_emails(users)
        for email in emails:
            if output_handle:
                output_handle.write(email + "\n")
                output_handle.flush()

# Class for scanning a folder and extracting URLs from its files
class URLScanner:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    # Extract URLs from a given text using regex
    def extract_urls(self, text):
        return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    # Scan folder and extract URLs from its files
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

# Class for getting information about IP addresses
class IPInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    # Get IP information using the ip-api.com API
    def get_ip_info(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = json.loads(response.content)

        if data["status"] == "success":
            result = f"{ip},{data['country']},{data['regionName']},{data['city']}"
            return result
        else:
            print(colored(f"Failed to retrieve information for IP: {ip}", "red"))
            return None

    # Process a list of IP addresses and get their information
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
# Class for getting information about domain names
class DomainInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    # Get the IP address of a domain name
    def get_domain_ip(self, domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.gaierror:
            print(colored(f"Failed to resolve the domain: {domain}", "red"))
            return None

    # Process a list of domain names and get their information
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
# Function for parsing command line arguments
def parse_arguments():
    parser = ColoredArgumentParser(description='Get IP information and save to a file.')
    parser.add_argument('-iplist', help='Path to the file containing the list of IP addresses.')
    parser.add_argument('-ip', help='A single IP address to get information.')
    parser.add_argument('-d', '--domain', help='A single domain name to get information.')
    parser.add_argument('-dlist', help='Path to the file containing the list of domain names.')
    parser.add_argument('-url', help='Path to the folder containing files to scan for URLs.')
    parser.add_argument('-o', '--output-file', help='Path to the output file.')
    parser.add_argument('-egen', help='Path to the file containing the firstname and lastname pairs.')
    parser.add_argument('-edom', help='The email domain to be used for generating email addresses.')
    return parser.parse_args()

# Function for processing URL scans
def process_url_scan(folder_path, output_handle):
    scanner = URLScanner(folder_path)
    urls = scanner.scan_folder()

    for url in urls:
        print(url)
        if output_handle:
            output_handle.write(url + "\n")
            output_handle.flush()

# Main function for handling command line arguments and processing input
def main():
    args = parse_arguments()
    input_file = args.iplist
    single_ip = args.ip
    domain = args.domain
    domain_list = args.dlist
    folder_path = args.url
    output_file = args.output_file
    firstname_lastname_list = args.egen
    email_domain = args.edom

    output_handle = open(output_file, "w") if output_file else None

    # Process input based on the provided command line arguments
    if firstname_lastname_list and email_domain:
        email_generator = EmailGenerator(firstname_lastname_list, email_domain)
        email_generator.process_name_list(output_handle)
    elif input_file:
        ip_info = IPInfo(output_handle)
        ip_info.process_ip_list(input_file)
    elif domain_list:
        domain_info = DomainInfo(output_handle)
        domain_info.process_domain_list(domain_list)
    elif single_ip:
        ip_info = IPInfo(output_handle)
        result = ip_info.get_ip_info(single_ip)
        if result:
            print(result)
            if output_handle:
                output_handle.write(result + "\n")
                output_handle.flush()
    elif domain:
        domain_info = DomainInfo(output_handle)
        ip = domain_info.get_domain_ip(domain)
        if ip:
            ip_info = IPInfo(output_handle)
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

    # Close output_handle if it was opened
    if output_handle:
        output_handle.close()

if __name__ == '__main__':
    main()
