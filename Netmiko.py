from netmiko import ConnectHandler

CSR1000v = {
    'device_type': 'cisco_ios',
    'host':   '192.168.56.4',
    'username': 'cisco',
    'password': 'cisco123!'
}

try:
    net_connect = ConnectHandler(**CSR1000v)
    print("Copiando comandos...\n...\n...")
except Exception as e:
    print(f"Ta malo: {e}")
    exit()
    
commands = [
    'router ospf 1',
    'router-id 1.1.1.1',
    'network 33.33.33.33 0.0.0.0 area 0',
    'passive-interface GigabitEthernet1',
    'exit',
    'ipv6 unicast-routing',
    'router ospfv3 1',
    'router-id 1.1.1.1',
    'address-family ipv6 unicast',
    'exit',
    'interface loopback 44',
    'ipv6 enable',
    'ipv6 ospf 1 area 0',
    'exit'
]

try:
    output = net_connect.send_config_set(commands)
    print(output)
    print("parece que funcionó...\n")
except Exception as g:
    print(f"TA MALO OSPF: {g}")
    net_connect.disconnect()
    exit()
    
show_commands = [
    'show running-config | section ospf',
    'show ip interface brief',
    'show running-config',
    'show version'
]

for command in show_commands:
    try:
        output = net_connect.send_command(command)
        print(f"¿Que tal un {command}?\n{output}\n\nmish...\n\n")
    except Exception as l:
        print(f"Error al ejecutar {command}: {l}")
net_connect.disconnect()


