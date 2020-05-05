import threading
import time
from my_devices import devices
from my_functions import ssh_command

start = time.time()

for device in devices: 
    my_thread = threading.Thread(target=ssh_command, args=(device, "show version"))
    my_thread.start()

main_thread = threading.currentThread()
for thread in threading.enumerate():
    if thread != main_thread: 
        thread.join()

end = time.time()

print(f"Total Elapsted Time: {end-start}")
