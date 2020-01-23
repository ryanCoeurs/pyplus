from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(host='nxos1.lasthop.io', username='pyclass', password=getpass(), device_type='cisco_nxos')

print(net_connect.find_prompt())
