"""
6. Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows: 

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
Execute the following sequence of events using Netmiko:
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel. Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt(). The enable() method will use the 'secret' defined in your device definition. This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.

"""

from netmiko import ConnectHandler
from getpass import getpass
import time 

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}


net_connect = ConnectHandler(**device)
#a
print(net_connect.find_prompt())
#b
net_connect.config_mode()
print(net_connect.find_prompt())
#c
net_connect.exit_config_mode()
print(net_connect.find_prompt())
#d
net_connect.write_channel('disable\n')
#e
time.sleep(2)
print(net_connect.read_channel())
#f
net_connect.enable()
print(net_connect.find_prompt())


