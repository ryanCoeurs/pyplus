"""
1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
"""

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
device  = {
    "host": 'cisco4.lasthop.io', 
    "username": 'pyclass',
    "password": password, 
    "device_type": 'cisco_ios'
}


net_connect = ConnectHandler(**device)

#Exercise 1.a
net_connect.send_command_timing('ping')
#ip
net_connect.send_command_timing('ip')
#target
net_connect.send_command_timing('8.8.8.8')
#repeat
net_connect.send_command_timing('5')
#datagram size
net_connect.send_command_timing('100')
#timeout
net_connect.send_command_timing('3')
#extended?
net_connect.send_command_timing('n')
#sweep sizes?
output = net_connect.send_command_timing('n')

print("1.a Output:")
print(output)

#Exercise 1.b
net_connect.send_command('ping', expect_string=r':')
#ip
net_connect.send_command('ip', expect_string=r':')
#target
net_connect.send_command('8.8.8.8', expect_string=r':')
#repeat
net_connect.send_command('5', expect_string=r':')
#datagram size
net_connect.send_command('100', expect_string=r':')
#timeout
net_connect.send_command('3', expect_string=r':')
#extended?
net_connect.send_command('n', expect_string=r':')
#sweep sizes?
output = net_connect.send_command('n', expect_string=r'#')

print("1.b Output:")
print(output)
