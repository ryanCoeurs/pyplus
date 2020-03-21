"""
Copy of 2.py because I can't import a file starting with a numeral for exercise 4
Also added __main__ for better importing
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


if __name__== "__main__":
    device = Device(**srx2)
    device.open()

    route_table = gather_routes(device)
    arp_table = gather_arp_table(device)
    print_output (device, route_table, arp_table)
