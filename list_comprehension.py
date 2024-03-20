# numbers = [1, 2, 3, 4, 5]
# squares = [n**2 for n in numbers]
# print(squares)  # Output: [1, 4, 9, 16, 25]


# evens = [n for n in numbers if n % 2 == 0]
# print(evens)  # Output: [2, 4]

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Output: [2, 4]

# ip_list = ["192.168.1.1", "10.0.0.256", "172.16.0.1", "256.0.0.1"]
# valid_ips = [ip for ip in ip_list if 0 <= int(ip.split('.')[0]) <= 255]
# print(valid_ips)  # Output: ['192.168.1.1', '172.16.0.1']


ip_list = ["192.168.1.1", "10.0.0.256", "172.16.0.1", "256.0.0.1"]
valid_ips = [ip for ip in ip_list if all(0 <= int(octet) <= 255 for octet in ip.split('.'))]
print(valid_ips)  # Output: ['192.168.1.1', '172.16.0.1']


interfaces = [f"GigabitEthernet0/{i}" for i in range(0, 5)]
print(interfaces)
# Output: ['GigabitEthernet0/0', 'GigabitEthernet0/1', ..., 'GigabitEthernet0/4']


subnets = [["192.168.1.1", "192.168.1.2"], ["10.0.0.1", "10.0.0.2"]]
all_ips = [ip for subnet in subnets for ip in subnet]
print(all_ips)
# Output: ['192.168.1.1', '192.168.1.2', '10.0.0.1', '10.0.0.2']





