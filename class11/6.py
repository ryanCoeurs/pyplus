import requests
import json
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

import os
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Created ID from excercise 4
new_id = 172

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

new_url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{new_id}/"
response = requests.delete(new_url, headers=http_headers, verify=False)

print("HTTP Status Code")
print(response.status_code)




