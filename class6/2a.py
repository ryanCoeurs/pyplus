"""
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""

import os
import pyeapi
from getpass import getpass
import yaml

with open("2a.yml") as file:
    inventory = yaml.full_load(file)

password = getpass()

for device, device_dict in inventory.items():
    device_dict['password'] = password

    connection = pyeapi.client.connect(**device_dict)
    device_api = pyeapi.client.Node(connection)
    arp_table = device_api.run_commands("show ip arp")

    arp_table = arp_table[0]

    for entry in arp_table['ipV4Neighbors']:
        print(f"{entry['address']}: {entry['hwAddress']} ")

