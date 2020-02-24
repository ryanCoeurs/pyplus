from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("2b.j2")

nxos1 = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.1", 
    "netmask": "24", 
    "peer_ip": "10.1.100.2",
    "local_as": "22"
}

nxos2 = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.2", 
    "netmask": "24",
    "peer_ip": "10.1.100.1",
    "local_as": "22"
}

devices = [nxos1, nxos2]

for device in devices:
    print(template.render(**device))
