from getpass import getpass
from netmiko import ConnectHandler
import pytest


@pytest.fixture(scope = "module")

def netmiko_connect(request):
    password = getpass()
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    connection = ConnectHandler(**arista1)
    
    def finalizer():
        connection.disconnect()

    request.addfinalizer(finalizer)
    return connection

