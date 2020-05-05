from concurrent.futures import ThreadPoolExecutor, wait
import time
from my_devices import devices
from my_functions import ssh_command2

start = time.time()

pool = ThreadPoolExecutor()
futures = []

for device in devices: 
    futures.append(pool.submit(ssh_command2, device, "show version"))

wait(futures)

for future in futures: 
    print()
    print(future.result())
    print()

end = time.time()

print(f"Total Elapsted Time: {end-start}")
