"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

from colored_argument_parser import ColoredArgumentParser
from email_generator import EmailGenerator
from url_scanner import URLScanner
from ip_info import IPInfo
from domain_info import DomainInfo
from termcolor import colored
from godaddy_search import query_similar_domains
from dorks_search import google_dork
from holehe import EmailProfiler



# Function for parsing command line arguments
def parse_arguments():
    parser = ColoredArgumentParser(description='Get IP information and save to a file.')
    parser.add_argument('-iplist', help='Specify a file with IPs, 1 per line, to get their COUNTRY|CITY|AREA.')
    parser.add_argument('-ip', help='Specify an IP to get its COUNTRY|CITY|AREA.')
    parser.add_argument('-d', '--domain', help='Specify a Domain to get its IP|COUNTRY|CITY|AREA.')
    parser.add_argument('-dlist', help='Specify a file with Domains, 1 per line, to get their IP|COUNTRY|CITY|AREA.')
    parser.add_argument('-url', help='Specify a folder path to get all URLs inside its files')
    parser.add_argument('-o', '--output-file', help='Name of the output file.')
    parser.add_argument('-egen', help='Path to the file containing the firstname and lastname pairs.')
    parser.add_argument('-edom', help='Specify a domain name to be combined with the names specified with -egen')
    parser.add_argument('-daddy', help='Specify a domain and get other available domain suffixes on GoDaddy.com.')
    parser.add_argument('-domphish', help='Search for similarly looking domains for a user supplied domain.')
    parser.add_argument('-dork', help='Specify a domain name for Google Dork search.')
    parser.add_argument('-f', help='Specify a file containing Google dorks (one per line).')
    parser.add_argument('-mails', help='Specify a file containing the emails to be profiled.')

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
    gdork_domain = args.dork
    gdork_file = args.f
    email_file = args.mails
    
    output_handle = open(output_file, "w") if output_file else None

    if args.domphish:
        # Define the character replacements here
        replacements = {
            'o': '0',
            '0': 'o',
            'i': 'l',
            'l': 'i',
            'g': 'q',
            'q': 'g',
            'm': 'n',
            'n': 'm',
            'u': 'v',
            'v': 'u',
            '1': 'l',
            'l': '1',
        }
        query_similar_domains(args.domphish, replacements)
        return

    if firstname_lastname_list and email_domain:
        email_generator = EmailGenerator(firstname_lastname_list, email_domain)
        email_generator.process_name_list(output_handle)
        return
    
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

    elif args.daddy:
        query_similar_domains(args.daddy)
    
    elif gdork_domain and gdork_file:
        google_dork(gdork_domain, gdork_file)

    if email_file:
        profiler = EmailProfiler(email_file)
        profiler.profile()
    elif firstname_lastname_list and email_domain:
        email_generator = EmailGenerator(firstname_lastname_list, email_domain)
        email_generator.process_name_list(output_handle)

    else:
        print(colored("Go quickly to the help section (-h), you really screwed the pooch.", "yellow"))

    if output_handle:
        output_handle.close()

if __name__ == '__main__':
    main()
