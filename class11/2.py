import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = "https://netbox.lasthop.io/api/"
response = requests.get(url, verify=False)

print("2a")
print("HTTP Status Code:")
print(response.status_code)
print("Response Text:")
print(response.text)
print("JSON Response")
print(response.json())
print("HTTP Rresponse Headers")
print(response.headers)


http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
response = requests.get(url, headers=http_headers, verify=False)

print("2b")
print("HTTP Status Code:")
print(response.status_code)
print("Response Text:")
print(response.text)
print("JSON Response")
print(response.json())
print("HTTP Rresponse Headers")
print(response.headers)

print("2c")
url = "https://netbox.lasthop.io/api/dcim/"
response = requests.get(url, headers=http_headers, verify=False)
pprint(response.json())
