from colored_argument_parser import ColoredArgumentParser
from email_generator import EmailGenerator
from url_scanner import URLScanner
from ip_info import IPInfo
from domain_info import DomainInfo
from termcolor import colored
from godaddy_search import query_similar_domains


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
    parser.add_argument('-daddy', help='The domain to search for similar domains using GoDaddy API.')

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

    elif args.daddy:
        query_similar_domains(args.daddy)

    else:
        print(colored("Please provide either a single IP (-ip), a domain (-d), a list of IPs (-iplist), a list of domains (-dlist), or a folder to scan for URLs (-url).", "yellow"))

    if output_handle:
        output_handle.close()

if __name__ == '__main__':
    main()
