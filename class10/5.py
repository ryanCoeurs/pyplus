from concurrent.futures import ProcessPoolExecutor, as_completed
import time
from my_devices import devices
from my_functions import ssh_command2

start = time.time()

futures = []

with ProcessPoolExecutor(6) as pool:
    for device in devices: 
        futures.append(pool.submit(ssh_command2, device, "show version"))

    for future in as_completed(futures): 
        print()
        print(future.result())
        print()

end = time.time()

print(f"Total Elapsted Time: {end-start}")
