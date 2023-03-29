import itertools
import requests

def generate_similar_domains(domain, num_domains=3):
    words = domain.split(".")[0].split("-")
    tlds = [".com", ".net", ".org", ".io", ".co"]
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
    api_key = 'gHVWzYDGHTs5_PJ63J1MtGbZmxZoxcb2iyK'
    api_secret = 'FDqRjsyoSor5n1M8ypNFfS'

    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
    }

    url = f'https://api.godaddy.com/v1/domains/available?domain={domain}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        domain_info = response.json()
        return domain_info['available']
    else:
        return None

def query_similar_domains(domain):
    similar_domains = generate_similar_domains(domain)

    for domain in similar_domains:
        is_available = check_domain_availability(domain)
        if is_available is None:
            print(f"Error occurred while checking {domain}")
        else:
            print(f"{domain} is {'available' if is_available else 'not available'}")
