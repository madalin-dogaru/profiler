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
    similar_domains = generate_similar_domains(domain, num_domains=10)
    check_availability(similar_domains)

def generate_similar_domains(domain):
    substitutions = {
        'o': '0',
        'l': '1',
        'i': '1',
        'a': '4',
        's': '5',
        't': '7',
    }

    name, tld = domain.rsplit('.', 1)
    last_two_chars = name[-2:]
    name_prefix = name[:-2]

    result = []

    for i, char1 in enumerate(last_two_chars):
        for char2 in substitutions.get(char1, char1):
            new_word = name_prefix + last_two_chars[:i] + char2 + last_two_chars[i + 1:] + '.' + tld
            result.append(new_word)

    return result

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
