"""
2. xmltodict basics

2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. Print out this new variable and its type. Note, the newly created object is an OrderedDict; not a traditional dictionary.


2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. Your output should look similar to the following (tip, enumerate will probably help): 

Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
"""
import xmltodict
from pprint import pprint

#security_zones_tree = ""
with open("show_security_zones.xml") as file:
    security_zones_dict = xmltodict.parse(file.read())


print("2a")
print("")
pprint(security_zones_dict)
print(type(security_zones_dict))

print("")
print("2b")
print("")
zones = security_zones_dict['zones-information']
zones = zones['zones-security']
for index, zone_data in enumerate(zones):
    print(f"Security Zone #{index+1}: {zone_data['zones-security-zonename']}")
