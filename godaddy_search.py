import requests
from typing import List

def generate_similar_domains(domain: str) -> List[str]:
    domain_parts = domain.split('.')
    domain_name = domain_parts[0]
    domain_suffix = domain_parts[1]

    similar_domains = []
    common_suffixes = ['com', 'net', 'org', 'info', 'co', 'io']

    # 5 similar domains with different suffixes
    for suffix in common_suffixes:
        if suffix != domain_suffix:
            similar_domains.append(f'{domain_name}.{suffix}')
            if len(similar_domains) >= 5:
                break

    return similar_domains

def generate_domain_variations(domain: str) -> List[str]:
    domain_parts = domain.split('.')
    domain_name = domain_parts[0]

    substitutions = {
        'i': 'l',
        'l': 'i',
        'o': '0',
        '0': 'o',
    }

    variations = set()
    for i, char in enumerate(domain_name[::-1]):
        if char in substitutions:
            new_char = substitutions[char]
            new_domain_name = domain_name[:-(i + 1)] + new_char + domain_name[-i:]
            variations.add(f'{new_domain_name}.{domain_parts[1]}')
            if len(variations) >= 5:
                break

    return list(variations)

def query_similar_domains(domain: str):
    api_key = 'gHVWzYDGHTs5_PJ63J1MtGbZmxZoxcb2iyK'
    api_secret = 'FDqRjsyoSor5n1M8ypNFfS'

    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
    }

    similar_domains = generate_similar_domains(domain)
    domain_variations = generate_domain_variations(domain)

    all_domains = similar_domains + domain_variations

    for domain in all_domains:
        url = f'https://api.godaddy.com/v1/domains/available?domain={domain}'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            domain_info = response.json()
            print(f"{domain} is {'available' if domain_info['available'] else 'not available'}")
        else:
            print(f"Error occurred: {response.status_code} - {response.text}")
