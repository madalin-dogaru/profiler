"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

import itertools
import requests
from termcolor import colored

def generate_similar_domains(domain, num_domains = 10):
    words = domain.split(".")[0].split("-")
    tlds = [".com", ".net", ".org", ".io", ".co", ".ai", ".us", ".de"]
    similar_domains = set()

    for tld in tlds:
        for perm in itertools.permutations(words):
            similar_domain = "-".join(perm) + tld
            if similar_domain != domain:
                similar_domains.add(similar_domain)
                if len(similar_domains) >= num_domains:
                    return similar_domains

    return similar_domains

def check_domain_availability(domain):
    api_key = 'your_api_key'
    api_secret = 'your_secret'

    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
    }

    url = f'https://api.godaddy.com/v1/domains/available?domain={domain}'

    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        domain_info = response.json()
        return domain_info['available']
    else:
        return None

def replace_domain_characters(domain, replacements):
    replaced_domains = []
    domain_name, tld = domain.rsplit(".", 1)
    for index, char in enumerate(domain_name):
        if char in replacements:
            replacement = replacements[char]
            new_domain_name = domain_name[:index] + replacement + domain_name[index + 1:]
            new_domain = new_domain_name + "." + tld
            replaced_domains.append(new_domain)
    return replaced_domains


def query_similar_domains(domain, replacements = None):
    if replacements:
        replaced_domains = replace_domain_characters(domain, replacements)
        for replaced_domain in replaced_domains:
            is_available = check_domain_availability(replaced_domain)
            if is_available is None:
                print(f"Error occurred while checking {replaced_domain}")
            else:
                if is_available:
                    print(colored(f"{replaced_domain} is available", 'green'))
                else:
                    print(colored(f"{replaced_domain} is not available", 'red'))
    else:
        similar_domains = generate_similar_domains(domain)

        for domain in similar_domains:
            is_available = check_domain_availability(domain)
            if is_available is None:
                print(f"Error occurred while checking {domain}")
            else:
                if is_available:
                    print(colored(f"{domain} is available", 'green'))
                else:
                    print(colored(f"{domain} is not available", 'red'))
