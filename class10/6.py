from concurrent.futures import ProcessPoolExecutor, as_completed
import time
from my_devices import devices
from my_functions import ssh_command2

start = time.time()



with ProcessPoolExecutor(6) as pool:
    
    commands = []

    for device in devices:
        command = "show ip arp"
        if "junos" in device["device_type"]:
            command = "show arp"
        commands.append(command)

    results_generator = pool.map(ssh_command2, devices, commands)

    for result in results_generator: 
        print()
        print(result)
        print()

end = time.time()

print(f"Total Elapsted Time: {end-start}")
