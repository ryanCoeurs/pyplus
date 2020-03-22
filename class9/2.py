"""
2. NAPALM Getters

2a. Create a new file named "my_functions.py" that will store a set of reusable functions. Move the "open_napalm_connection" function from exercise1 into this Python file. Import the network devices once again from my_devices.py and create a list of connection objects (once again with connections to both cisco3 and arista1).

2b. Pretty print the arp table for each of these devices. Gather this information using the appropriate NAPALM Getter.

2c. Attempt to use the get_ntp_peers() method against both of the devices. Does this method work? Your code should gracefully handle any exceptions that occur. In other words, an exception that occurs due to this get_ntp_peers() method, should not cause the program to crash.

2d. Create another function in "my_functions.py". This function should be named "create_backup" and should accept a NAPALM connection object as an argument. Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file. The filename should be unique for each device. In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration. Note, get_config() returns a dictionary where the running-config is referenced using the "running" key. Call this function as part of your main exercise2 and ensure that the configurations from both cisco3 and arista1 are backed up properly.
"""
from my_devices import inventory
from napalm import get_network_driver
from pprint import pprint
from my_functions import napalm_connect, create_backup

#2a
connection_objects = []
for device in inventory:
    connection = napalm_connect(device)
    connection_objects.append(connection)

#2b 
for connection in connection_objects: 
    print(connection.hostname)
    pprint(connection.get_arp_table())
 
#2c
for connection in connection_objects: 
    try: 
        print(connection.hostname)
        print(connection.get_ntp_peers())
    except Exception as e:
        print(e) 

#2d
for connection in connection_objects: 
    create_backup(connection)

