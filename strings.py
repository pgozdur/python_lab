single_quoted_string = 'Hello, Python!'
double_quoted_string = "Hello, Python!"
print(single_quoted_string)
print(double_quoted_string)

greeting = "Hello"

target = "World"
message = greeting + ", " + target + "!"
print(message)  # Output: Hello, World!


name = "Python"
version = 3.8
message = f"Welcome to {name} version {version}!"
print(message)  # Output: Welcome to Python version 3.8!

a = 5
b = 10
result_message = f"The sum of {a} and {b} is {a + b}."
print(result_message)  # Output: The sum of 5 and 10 is 15.

length = len(message)
print(length)  # Output: 13

cidr_notation = "172.168.1.1/24"
ip_address = cidr_notation.split('/')[0]
print(ip_address)  # Output: 172.168.1.1


first_octet = ip_address[:ip_address.index('.')]
print(first_octet)  # Output: 172

second_octet_start = ip_address.index('.') + 1
second_octet_end = ip_address.index('.', second_octet_start)
second_octet = ip_address[second_octet_start:second_octet_end]
print(second_octet)  # Output: 168


subnet_mask = cidr_notation.split('/')[1]
print(subnet_mask)  # Output: 24




