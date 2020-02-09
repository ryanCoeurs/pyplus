"""
5. In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.
"""
from pathlib import Path
import yaml
from netmiko import ConnectHandler

home = str(Path.home())
input_file = home + "/.netmiko.yml"

f = open(input_file)
inventory = yaml.load(f)



net_connect = ConnectHandler(**inventory['cisco3'])
print(net_connect.find_prompt())


