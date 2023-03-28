import argparse
import requests

API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
GODADDY_API_ENDPOINT = 'https://api.godaddy.com/v1/domains/available'

def query_similar_domains(domain):
    headers = {
        'Authorization': f'sso-key gHVWzYDGHTs5_PJ63J1MtGbZmxZoxcb2iyK:FDqRjsyoSor5n1M8ypNFfS',
        'Accept': 'application/json'
    }
    params = {
        'domain': domain,
        'checkType': 'FAST',
        'forTransfer': 'false',
        'tlds': 'com,net,org'
    }

    response = requests.get(GODADDY_API_ENDPOINT, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['available']:
            print(f"{domain} is available.")
        else:
            print(f"{domain} is not available.")
    else:
        print(f"Error: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description='Query for domains similar to the one specified by the user.')
    parser.add_argument('-daddy', type=str, required=True, help='The domain to search for similar domains.')
    args = parser.parse_args()

    query_similar_domains(args.daddy)

if __name__ == '__main__':
    main()
