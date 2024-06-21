"""
This script is used to fetch the Record ID of a given DNS record from Cloudflare.

It uses the Cloudflare API to fetch the Record ID, which is a unique identifier for a DNS record in Cloudflare.

Environment Variables:
    API_TOKEN: The API token for your Cloudflare account.
    ZONE_ID: The ID of the zone (domain) you want to fetch the Record ID from.
    RECORD_NAME: The name of the DNS record you want to fetch the Record ID for.

Functions:
    get_record_id(zone_id, record_name): Fetches and returns the Record ID for the given DNS record.

This script is meant to be run when you need to fetch the Record ID for a DNS record. The Record ID is required for many operations in the Cloudflare API, such as updating DNS records.
"""

from dotenv import load_dotenv
load_dotenv()
import requests
import os

API_TOKEN = os.getenv('API_TOKEN')
ZONE_ID = os.getenv('ZONE_ID')
RECORD_NAME = os.getenv('RECORD_NAME')

def get_record_id(zone_id, record_name):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {'name': record_name}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        records = response.json()['result']
        if records:
            return records[0]['id']
        else:
            print("No DNS records found for the given name.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching Record ID: {e}")
        return None

record_name = RECORD_NAME
record_id = get_record_id(ZONE_ID, record_name)
if record_id:
    print(f"Record ID for {record_name}: {record_id}")
else:
    print("Failed to retrieve Record ID.")
