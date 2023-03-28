import requests
from typing import List
from domain_generator import generate_similar_domains, generate_domain_variations

def check_domain_availability(domain: str, headers: dict) -> bool:
    url = f'https://api.godaddy.com/v1/domains/available?domain={domain}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        domain_info = response.json()
        return domain_info['available']
    else:
        print(f"Error occurred: {response.status_code} - {response.text}")
        return False

def query_similar_domains(domain: str):
    api_key = 'gHVWzYDGHTs5_PJ63J1MtGbZmxZoxcb2iyK'
    api_secret = 'FDqRjsyoSor5n1M8ypNFfS'

    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
    }

    similar_domains = generate_similar_domains(domain)
    domain_variations = generate_domain_variations(domain)
    unique_domains = list(set(similar_domains + domain_variations))

    for domain in unique_domains:
        is_available = check_domain_availability(domain, headers)
        print(f"{domain} is {'available' if is_available else 'not available'}")
