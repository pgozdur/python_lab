ip_addresses = ['192.168.1.1', '10.0.0.1', '172.16.0.1']
for ip in ip_addresses:
    print(ip)


command = "show ip interface brief"
for char in command:
    print(char)


interfaces = {'GigabitEthernet0': 'up', 'GigabitEthernet1': 'down'}
for interface, status in interfaces.items():
    print(f"Interface {interface} is {status}")

for i in range(5):  # 0 to 4
    print(f"Interface GigabitEthernet0/{i}")

counter = 0
while counter < 5:
    print(f"Counter is {counter}")
    counter += 1
# Important to modify the loop condition to avoid an infinite loop


counter = 0
while True:  # Infinite loop
    print(f"Counter is {counter}")
    counter += 1

