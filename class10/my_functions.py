from netmiko import ConnectHandler

def ssh_command( device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    print()
    print(output)
    print()

def ssh_command2( device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    return output
