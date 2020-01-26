"""
2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.
"""

from netmiko import ConnectHandler
from getpass import getpass
import datetime

password = getpass()
device  = {
    "host": 'nxos2.lasthop.io', 
    "username": 'pyclass',
    "password": password, 
    "device_type": 'cisco_nxos', 
    "global_delay_factor": 2
}


net_connect = ConnectHandler(**device)

start = datetime.datetime.now()
print(net_connect.send_command('show lldp neighbors detail'))
end = datetime.datetime.now()
print(f"Execution time: {(end-start).seconds} seconds")

start = datetime.datetime.now()
print(net_connect.send_command('show lldp neighbors detail', delay_factor=8))
end = datetime.datetime.now()
print(f"Execution time: {(end-start).seconds} seconds")
