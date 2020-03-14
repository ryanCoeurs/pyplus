"""
1. Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses
"""

import os
import pyeapi
from getpass import getpass

device = {
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "port": 443,
    "transport": "https"
}

connection = pyeapi.client.connect(**device)
device_api = pyeapi.client.Node(connection)
arp_table = device_api.run_commands("show ip arp")

arp_table = arp_table[0]

for entry in arp_table['ipV4Neighbors']:
    print(f"{entry['address']}: {entry['hwAddress']} ")

