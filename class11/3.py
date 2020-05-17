import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

import os
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

print("3a")
url = "https://netbox.lasthop.io/api/dcim/devices/"
response = requests.get(url, headers=http_headers, verify=False)
devices = response.json()["results"]
for device in devices:
    print(device["display_name"])


print("3b")
def print_device(device):
    print("-" * 40)
    print(device["display_name"])
    print("-" * 10)
    print(f"Location: {device['site']['name']}")
    print(f"Vendor: {device['device_type']['manufacturer']['name']}")
    print(f"Status: {device['status']['label']}")
    print("-" * 40)
    print()

for device in devices:
    print_device(device)
