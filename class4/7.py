"""
7. Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data. In this Python program, read the show interface status data from a file and process it using the TextFSM template. From this parsed-output, create a list of dictionaries. The program output should look as follows: 

$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
"""
import textfsm
from pprint import pprint

template_file = "2.template"
template = open(template_file)
template = textfsm.TextFSM(template)

with open("2.input") as f:
    interface_input = f.read()

interfaces = template.ParseText(interface_input)

output = []
for interface in interfaces:
    print (interface[0])
    int_dict = {
        'DUPLEX': interface[3], 
        'PORT_NAME': interface[0], 
        'PORT_TYPE': interface[5],
        'SPEED': interface[4], 
        'STATUS': interface[1], 
        'VLAN': interface[2]
    }
    output.append(int_dict)

pprint(output)
