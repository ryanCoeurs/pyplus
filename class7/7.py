"""
7. NX-API using XML and the nxapi_plumbing library

7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "xml" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500


7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands: "show system uptime" and "show system resources". Print the XML output from these two commands.


7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions. Pick random loopback interface numbers between 100 and 199.
"""
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
print("7a")
print("")
interface = output.find(".//interface").text
state = output.find(".//state").text
mtu = output.find(".//eth_mtu").text
print (f"Interface: {interface}; State: {state}; MTU: {mtu}")

print("")
print("7b")
print("")
output = device.show("show system uptime", "show system resources")
for result in output:
    print(etree.tostring(result).decode())

print ("")
print("7c")
print("")
config = [
    "interface loopback111",
    "description first excercise 7c loopback",
    "interface loopback133",
    "description loopback133 7c exercise"
]
output = device.config_list(config)

