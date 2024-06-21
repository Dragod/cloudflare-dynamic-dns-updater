# Update A record

Update all the subdomain of a given domain to point to the current isp ip address on the "A" record on cloudflare DNS
Really handy to keep localhost docker container up 24/7 without a static IP address

## Script run order

- get-zone-id.py
- get-record-id.py
- update-a-record-win/unix.py

```bash
# .env file (you need to create it, not in git)
API_TOKEN = 'apitokenhere'
ZONE_ID = 'zonedidhere'
RECORD_ID = 'recordidhere'
RECORD_NAME = '*'
DOMAIN = 'domain.com'
```
