import os
from getpass import getpass
import yaml


def get_inventory():
    with open("2a.yml") as file:
        inventory = yaml.full_load(file)

    password = getpass()

    for device, device_dict in inventory.items():
        device_dict['password'] = password

    return inventory

def print_table(arp_table):
    for entry in arp_table['ipV4Neighbors']:
        print(f"{entry['address']}: {entry['hwAddress']} ")

