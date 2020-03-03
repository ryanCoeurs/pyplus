from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("4.j2")

vrfs = []
for x in range(1,6):
    variables = {
        "vrf_name": f"blue{x}", 
        "rd_number": f"100:{x}", 
        "ipv4_enabled": True, 
        "ipv6_enabled": True
    }
    vrfs.append(variables)

template_vrfs = {"vrfs": vrfs}

print(template.render(**template_vrfs))
