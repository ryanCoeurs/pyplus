"""
4. Replace Operations

4a. Add nxos1 to your my_devices.py file. Ensure that you include the necessary information to set the NX-API port to 8443. This is done using 'optional_args' in NAPALM so you should have the following key-value pair defined: 

"optional_args": {"port": 8443}

4b. Create a new function named 'create_checkpoint'. Add this function into your my_functions.py file. This function should take one argument, the NAPALM connection object. This function should use the NAPALM _get_checkpoint_file() method to retrieve a checkpoint from the NX-OS device. It should then write this checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file for configuration replace operations. Using this new function, retrieve a checkpoint from nxos1 and write it to the local file system.

4c. Manually copy the saved checkpoint to a new file and add an additional loopback interface to the configuration.

4d. Create a Python script that stages a complete configuration replace operation (using the checkpoint file that you just retrieved and modified). Once your candidate configuration is staged perform a compare_config (diff) on the configuration to see your pending changes. After the compare_config is complete, then use the discard_config() method to eliminate the pending changes. Next, perform an additional compare_config (diff) to verify that you have no pending configuration changes. Do not actually perform the commit_config as part of this exercise.
"""
from my_devices import nxos1
from napalm import get_network_driver
from pprint import pprint
from my_functions import napalm_connect, create_checkpoint

#4b
connection = napalm_connect(nxos1)
create_checkpoint(connection)

#4d
filename = f"{connection.hostname}.config.txt"
connection.load_replace_candidate(filename)
print("Config Diff:")
print(connection.compare_config())
connection.discard_config()
print("Config Diff Post Discard:")
print(connection.compare_config())
