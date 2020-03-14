"""
4. Note, this exercise might be fairly challenging. Construct a new YAML file that contains the four Arista switches. This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method. Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches:  

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file and should be associated with each individual Arista device. For example, here is what 'arista4' might look like in the YAML file:

arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches. Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
"""

import pyeapi
import os
from getpass import getpass
import yaml
from jinja2 import Template
from pprint import pprint

j2_template = """
interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}
"""

def get_inventory():
    with open("4.yml") as file:
        inventory = yaml.full_load(file)

    password = getpass()

    for device, device_dict in inventory.items():
        device_dict['password'] = password

    return inventory

inventory = get_inventory()

def generate_config(template, variables):   
    config = ""
    template = Template(template)
    return template.render(**variables)

for device, device_dict in inventory.items():
    connection = pyeapi.client.connect(**device_dict)
    device_api = pyeapi.client.Node(connection)
    
    config = generate_config(j2_template, device_dict['data']) 
    config = config.strip().splitlines()
    device_api.config(config)    

    ip_interfaces = device_api.enable("show ip interface brief")
    print(device)
    pprint(ip_interfaces[0]['result']['output'])
