from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("2a.j2")

nxos1 = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.1", 
    "netmask": "24"
}

nxos2 = {
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.2", 
    "netmask": "24"
}

devices = [nxos1, nxos2]

for device in devices:
    print(template.render(**device))
