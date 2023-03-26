import argparse
import requests
import json
import socket
import sys
from termcolor import colored


class ColoredArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (colored(self.prog, "red"), colored(message, "red")))

# Parse command line arguments
def parse_arguments():
    parser = ColoredArgumentParser(description='Get IP information and save to a file.')
    parser.add_argument('-iplist', help='Path to the file containing the list of IP addresses.')
    parser.add_argument('-ip', help='A single IP address to get information.')
    parser.add_argument('-d', '--domain', help='A single domain name to get information.')
    parser.add_argument('-dlist', help='Path to the file containing the list of domain names.')
    parser.add_argument('-o', '--output-file', help='Path to the output file.')
    return parser.parse_args()

# Get IP information from the IP-API
def get_ip_info(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = json.loads(response.content)

    if data["status"] == "success":
        result = f"{ip},{data['country']},{data['regionName']},{data['city']}"
        return result
    else:
        print(colored(f"Failed to retrieve information for IP: {ip}", "red"))
        return None

# Get the IP address of a domain
def get_domain_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print(colored(f"Failed to resolve the domain: {domain}", "red"))
        return None

# Process a file containing a list of IP addresses
def process_ip_list(input_file, output_handle):
    with open(input_file, "r") as ip_file:
        for line in ip_file:
            ip = line.strip()
            result = get_ip_info(ip)
            if result:
                print(result)
                if output_handle:
                    output_handle.write(result + "\n")
                    output_handle.flush()

# Process a file containing a list of domain names
def process_domain_list(domain_list, output_handle):
    with open(domain_list, "r") as domain_file:
        for line in domain_file:
            domain = line.strip()
            ip = get_domain_ip(domain)
            if ip:
                result = get_ip_info(ip)
                if result:
                    print(result)
                    if output_handle:
                        output_handle.write(result + "\n")
                        output_handle.flush()

# Main function
def main():
    # Parse command line arguments
    args = parse_arguments()
    input_file = args.iplist
    single_ip = args.ip
    domain = args.domain
    domain_list = args.dlist
    output_file = args.output_file

    # Process input file or domain list
    if input_file or domain_list:
        output_handle = open(output_file, "w") if output_file else None

        if input_file:
            process_ip_list(input_file, output_handle)
        elif domain_list:
            process_domain_list(domain_list, output_handle)

        if output_handle:
            output_handle.close()
    # Process single IP or domain
    elif single_ip:
        result = get_ip_info(single_ip)
        if result:
            if output_file:
                with open(output_file, "w") as file:
                    file.write(result + "\n")
                    file.flush()
            else:
                print(colored(result, "green"))
    elif domain:
        ip = get_domain_ip(domain)
        if ip:
            result = get_ip_info(ip)
            if result:
                if output_file:
                    with open(output_file, "w") as file:
                        file.write(result + "\n")
                        file.flush()
                else:
                    print(colored(result, "green"))
    else:
        print(colored("Please provide either a single IP (-ip), a domain (-d), a list of IPs (-iplist), or a list of domains (-dlist).", "yellow"))


if __name__ == '__main__':
    main()
