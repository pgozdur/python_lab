from netmiko import ConnectHandler
from pprint import pprint

cisco = {
    'device_type':'cisco_ios',
    'ip':'devnetsandboxiosxe.cisco.com',
    'username':'admin',     #ssh username
    'password':'C1sco12345',  #ssh password
}
  
net_connect = ConnectHandler(**cisco)

output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output)
