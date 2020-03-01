from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("2b.j2")

nxos1["variables"] = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.1", 
    "netmask": "24", 
    "peer_ip": "10.1.100.2",
    "local_as": "22"
}

nxos2["variables"] = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.2", 
    "netmask": "24",
    "peer_ip": "10.1.100.1",
    "local_as": "22"
}

devices = [nxos1, nxos2]

for device in devices:
    print (f"Configuring {device['host']}")
    cfg = template.render(**device['variables'])
    connect_device = device.copy()
    connect_device.pop('variables')
    net_connect = ConnectHandler(**connect_device)
    print (net_connect.send_config_set(cfg))
    

for device in devices:
    print (f"Testing {device['host']}")
    connect_device = device.copy()
    connect_device.pop('variables')
    net_connect = ConnectHandler(**connect_device)
    ping_cmd = f"ping {device['variables']['peer_ip']}"
    bgp_cmd = f"show ip bgp summary"

    print (net_connect.send_command(ping_cmd))
    print (net_connect.send_command(bgp_cmd))
    print("")
