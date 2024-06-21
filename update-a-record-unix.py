
"""
This script is used to update a wildcard A record in Cloudflare with the current public IP address of the machine it's run on.

It uses the Cloudflare API to update the record, and the ipify API to get the current public IP address.

Environment Variables:
    API_TOKEN: The API token for your Cloudflare account.
    ZONE_ID: The ID of the zone (domain) you want to update.
    RECORD_ID: The ID of the wildcard DNS record you want to update.
    RECORD_NAME: The wildcard record for subdomains.

Functions:
    get_public_ip(): Returns the current public IP address.
    update_a_record(new_ip): Updates the wildcard A record in Cloudflare with the new IP address.
    read_last_ip(file_path): Reads the last recorded IP address from a file.
    write_current_ip(file_path, ip): Writes the current IP address to a file.
    main(): The main function that orchestrates the IP address fetching and updating process.

This script is meant to be run periodically, to keep the A record in Cloudflare up-to-date with the machine's current public IP address.
A common use case is to run this script as a cron job on a server to keep a dynamic DNS record updated.
"""

from dotenv import load_dotenv
import requests
import os

# Cloudflare API credentials and details
API_TOKEN = os
ZONE_ID = os.getenv('ZONE_ID')
RECORD_ID = os.getenv('RECORD_ID')  # The ID of the wildcard DNS record you want to update
RECORD_NAME = os.getenv('RECORD_NAME')  # The wildcard record for subdomains
PROXIED = True  # Set to True if you want the record proxied by Cloudflare

# Function to get the current public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Check for HTTP errors
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None

# Function to update the wildcard A record in Cloudflare
def update_a_record(new_ip):
    url = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': RECORD_NAME,
        'content': new_ip,
        'ttl': 1,  # '1' stands for automatic TTL
        'proxied': PROXIED
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP errors
        print(f"A record updated successfully: {new_ip}")
    except requests.RequestException as e:
        print(f"Error updating A record: {e}")

# Function to read the last recorded IP address from a file
def read_last_ip(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

# Function to write the current IP address to a file
def write_current_ip(file_path, ip):
    with open(file_path, 'w') as file:
        file.write(ip)

def main():
    ip_file = 'current_ip.txt'

    current_ip = get_public_ip()

    if current_ip:
        last_ip = read_last_ip(ip_file)

        if current_ip != last_ip:
            print(f"IP address changed from {last_ip} to {current_ip}")
            update_a_record(current_ip)
            write_current_ip(ip_file, current_ip)
        else:
            print(f"IP address has not changed.")

if __name__ == "__main__":
    main()
