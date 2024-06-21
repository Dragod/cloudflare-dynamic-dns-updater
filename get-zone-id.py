"""
This script is used to fetch the Zone ID of a given domain from Cloudflare.

It uses the Cloudflare API to fetch the Zone ID, which is a unique identifier for a domain in Cloudflare.

Environment Variables:
    API_TOKEN: The API token for your Cloudflare account.
    DOMAIN_NAME: The domain name for which you want to fetch the Zone ID.

Functions:
    get_zone_id(domain_name): Fetches and returns the Zone ID for the given domain name.

This script is meant to be run when you need to fetch the Zone ID for a domain. The Zone ID is required for many operations in the Cloudflare API, such as updating DNS records.
"""

from dotenv import load_dotenv
import os
import requests

API_TOKEN = os.getenv('API_TOKEN')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

def get_zone_id(domain_name):
    url = 'https://api.cloudflare.com/client/v4/zones'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {'name': domain_name}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        zones = response.json()['result']
        if zones:
            return zones[0]['id']
        else:
            print("No zones found for the given domain.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching Zone ID: {e}")
        return None

domain_name = DOMAIN_NAME
zone_id = get_zone_id(domain_name)
if zone_id:
    print(f"Zone ID for {domain_name}: {zone_id}")
else:
    print("Failed to retrieve Zone ID.")
