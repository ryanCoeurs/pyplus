from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("3.j2")

variables = {
    "vrf_name": "blue", 
    "rd_number": "100:1", 
    "ipv4_enabled": True, 
    "ipv6_enabled": True
}

print(template.render(**variables))
