from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./")

template = env.get_template("5.j2")

variables = {
    "ntp_server1": "130.126.24.24", 
    "ntp_server2": "152.2.21.1", 
    "timezone": "PST", 
    "timezone_offset": "-8", 
    "timezone_dst": "PDT"
}

print(template.render(**variables))
