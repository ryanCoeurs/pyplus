from getpass import getpass

username = "pyclass"
password = getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username, 
    "password": password,
    "platform": "ios"
}


arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username, 
    "password": password,
    "platform": "eos"
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "nxos",
    "optional_args": {"port": 8443},
}

inventory = [cisco3, arista1]
