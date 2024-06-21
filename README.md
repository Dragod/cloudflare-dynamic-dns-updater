# Cloudflare DNS Management Scripts

This repository contains three Python scripts that interact with the Cloudflare API to manage DNS records:

1. `get-zone-id.py`: Fetches the Zone ID for a given domain.
2. `get-record-id.py`: Fetches the Record ID for a given DNS record.
3. `update-a-record.py`: Updates a wildcard A record with the current public IP address of the machine it's run on.

## Environment Variables

These scripts use the following environment variables:

- `API_TOKEN`: Your Cloudflare API token.
- `ZONE_ID`: The ID of the zone (domain) you want to interact with.
- `RECORD_ID`: The ID of the DNS record you want to interact with.
- `RECORD_NAME`: The name of the DNS record you want to interact with.

## Usage

First, set the environment variables with your Cloudflare details. (need to create a .env file in the repo root)

Then, you can run the scripts like this:

```bash
python get-zone-id.py
python get-record-id.py
python update-a-record.py
```

## Requirements

```bash
pip install requests python-dotenv
```

## Scheduled task on linux

```bash
# type on terminal
crontab -e
# Paste in the editor that did just open
# Run the script every minute to refresh the ip if changed)
*/1 * * * * /usr/bin/python3 /home/pi/cloudflare-dynamic-dns-updater/update-a-record-unix.py
```
