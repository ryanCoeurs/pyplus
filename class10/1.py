from netmiko import ConnectHandler
from my_devices import devices
import time

def single_command( device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    return output


start = time.time()

for device in devices: 
    print()
    print(single_command(device, "show version"))
    print()

end = time.time()    

print(f"Total Execution Time: {end -start}")

