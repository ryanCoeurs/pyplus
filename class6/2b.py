"""
2b. Create a Python module named 'my_funcs.py'. In this file create two functions: function1 should read the YAML file you created in exercise 2a and return the corresponding data structure; function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data). Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.
"""

import pyeapi
from my_funcs import get_inventory, print_table

inventory = get_inventory()

for device, device_dict in inventory.items():
    connection = pyeapi.client.connect(**device_dict)
    device_api = pyeapi.client.Node(connection)
    arp_table = device_api.run_commands("show ip arp")

    print_table(arp_table[0])
