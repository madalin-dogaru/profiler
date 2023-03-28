import itertools
import requests
from typing import List

api_key = 'gHVWzYDGHTs5_PJ63J1MtGbZmxZoxcb2iyK'
api_secret = 'FDqRjsyoSor5n1M8ypNFfS'

substitutions = {
    'o': '0',
    'l': 'I',
    'i': '1',

}

def query_similar_domains(domain: str):
    similar_domains = generate_similar_domains(domain, num_domains=20)
    check_availability(similar_domains)

def generate_similar_domains(domain: str, num_domains: int = 10) -> List[str]:
    domain_variation = character_substitution(domain)
    
    domains = [domain_variation]

    while len(domains) < num_domains:
        new_domain = character_substitution(domain)
        if new_domain not in domains:
            domains.append(new_domain)

    return domains

def character_substitution(word: str) -> str:
    last_two_chars = word[-2:]
    for original, replacement in substitutions.items():
        last_two_chars = last_two_chars.replace(original, replacement)
    return word[:-2] + last_two_chars

def check_availability(domains: List[str]):
    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
    }

    for domain in domains:
        url = f'https://api.godaddy.com/v1/domains/available?domain={domain}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            domain_info = response.json()
            print(f"{domain_info['domain']} is {'available' if domain_info['available'] else 'not available'}")
        else:
            print(f"Error occurred: {response.status_code} - {response.text}")
