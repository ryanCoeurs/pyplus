from napalm import get_network_driver

def napalm_connect(device_details):
    device_type = device_details.pop("platform")
    driver = get_network_driver(device_type)
    device = driver(**device_details)
    device.open()
    return device

def create_backup(device):
    config = device.get_config() 
    config = config["running"]
    filename = f"{device.hostname}.txt"  
    with open(filename, "w") as f:
        f.write(config)

def create_checkpoint(device):
    config = device._get_checkpoint_file()
    filename = f"{device.hostname}.txt"  
    with open(filename, "w") as f:
        f.write(config)
