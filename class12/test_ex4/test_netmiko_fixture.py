from getpass import getpass
from netmiko import ConnectHandler
import pytest


@pytest.fixture(scope = "module")

def netmiko_connect():
    password = getpass()
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    return ConnectHandler(**arista1)


def test_find_prompt(netmiko_connect):
    assert netmiko_connect.find_prompt() == "arista1#"


def test_show_version(netmiko_connect):
    assert "4.20.10M" in netmiko_connect.send_command("show version")
