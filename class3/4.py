"""
4. You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program. Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. Print this dictionary to standard output.

"""
import json

f = open("4input.json")
output = f.read()
arp_entries = json.loads(output)


result = {}
ipv4_neighbors = arp_entries['ipV4Neighbors']
for neighbor in ipv4_neighbors:
    ip = neighbor['address']
    mac = neighbor['hwAddress']
    result[ip]=mac

print (result)
