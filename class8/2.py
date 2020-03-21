"""
2. PyEZ Tables/Views:

2a. Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2". This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection. You should use getpass() for the password handling. You should import this "srx2" device definition for all of the remaining exercises in class8.

2b. Create a Python program that creates a PyEZ Device connection to "srx2" (using the previously created Python module). Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.
"""
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint

def check_connected(device):
    if device.connected:
        return True
    else:
        return False

def gather_routes(device):
    route_table = RouteTable(device)
    route_table.get()
    return route_table

def gather_arp_table(device):
    arp_table = ArpTable(device)
    arp_table.get()
    return arp_table

def print_output(device, route_table, arp_table):
    print(f"Hostname: {device.hostname}")
    print(f"NETCONF Port: {device.port}")
    print(f"Username: {device.user}")
    print(f"Route Table: ")
    pprint(route_table.items())
    print(f"Arp Table: ")
    pprint(arp_table.items())



device = Device(**srx2)
device.open()

route_table = gather_routes(device)
arp_table = gather_arp_table(device)
print_output (device, route_table, arp_table)
