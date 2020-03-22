"""

3. NAPALM Config Merge

3a. Using your existing functions and the my_devices.py file, create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`. In each of these files, create two new loopback interfaces with a description. Your files should be similar to the following: 

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration. In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change. Use the NAPALM compare_config() method to print out the pending differences (i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).
"""
from my_devices import inventory
from napalm import get_network_driver
from pprint import pprint
from my_functions import napalm_connect, create_backup

#3a
connection_objects = []
for device in inventory:
    connection = napalm_connect(device)
    connection_objects.append(connection)

#3b 
for connection in connection_objects: 
    filename = f"{connection.hostname}-loopbacks"
    connection.load_merge_candidate(filename)
    print(f"Hostname: {connection.hostname}")
    print(connection.compare_config())

#3c
for connection in connection_objects: 
    connection.commit_config()
    print(f"Hostname: {connection.hostname}")
    print(connection.compare_config())
