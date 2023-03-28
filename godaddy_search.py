import itertools
import requests
import random

def character_substitution(word):
    substitutions = {
        'o': '0',
        'l': 'L',
        'i': '1',
        
    }
    new_word = ''
    for char in word:
        new_char = substitutions.get(char, char)
        new_word += new_char if random.random() < 0.5 else char
    return new_word

def character_insertion(word):
    insertions = '0123456789'
    index = random.randint(0, len(word))
    return word[:index] + random.choice(insertions) + word[index:]

def generate_similar_domains(domain, num_domains=20):
    base_domain = domain.split(".")[0]
    tlds = [".com", ".net", ".org", ".io", ".co"]
    similar_domains = set()

    while len(similar_domains) < num_domains:
        for tld in tlds:
            altered_domain = base_domain
            if random.random() < 0.5:
                altered_domain = character_substitution(altered_domain)
            if random.random() < 0.5:
                altered_domain = character_insertion(altered_domain)

            similar_domain = altered_domain + tld
            if similar_domain != domain:
                similar_domains.add(similar_domain)
                if len(similar_domains) >= num_domains:
                    break

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
