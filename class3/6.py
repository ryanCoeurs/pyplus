"""
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface. Your solution should work if there is more than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work. The output from this program should look similar to the following: 

$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0

"""
from pathlib import Path
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home = str(Path.home())
input_file = home + "/.netmiko.yml"

f = open(input_file)
inventory = yaml.load(f)



net_connect = ConnectHandler(**inventory['cisco4'])
output = net_connect.send_command("show run")

config = CiscoConfParse(output.splitlines())

interfaces_with_address = config.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address" )

for interface in interfaces_with_address: 
    print (f"Interface Line: {interface.text}")
    #also catches secondary ip addresses
    addresses = interface.re_search_children(r"ip address")
    for address in addresses: 
        print (f"IP Address Line: {address.text}")


