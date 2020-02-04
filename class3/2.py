"""
2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices. The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?

"""

import yaml

device_names = ['cisco3', 'cisco4', 'arista1', 'arista2', 'arista3', 'arista4', 'srx2', 'nxos1', 'nxos2']
devices = []
for name in device_names:
    devices.append({
        "device_name": name,
        "host": f"{name}.lasthop.io",
        "username": "admin",
        "password": "fictional"
    }) 

#2a
print(devices)
#2b
with open("2b_output.yml", "w") as f:
    yaml.dump(devices, f, default_flow_style=False)
