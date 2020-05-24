from getpass import getpass
from netmiko import ConnectHandler



def netmiko_connect():
    password = getpass()
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    return ConnectHandler(**arista1)


def test_find_prompt():
    connection = netmiko_connect()
    assert connection.find_prompt() == "arista1#"


def test_show_version():
    connection = netmiko_connect()
    assert "4.20.10M" in connection.send_command("show version")
