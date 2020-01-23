from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
cisco3  = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass',
    "password": password, 
    "device_type": 'cisco_ios'
}


net_connect = ConnectHandler(**cisco3)
output = net_connect.send_command("show version")

f = open("netmiko3_show_version.txt", "w")
f.write(output)
f.close()
