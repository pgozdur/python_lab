def greet():
    print("Hello, Network Engineer!")

def configure_interface(interface_name, ip_address):
    print(f"Configuring {interface_name} with IP {ip_address}")


def calculate_metrics(bytes_transmitted, bytes_received):
    tx_rate = bytes_transmitted / 60  # Assuming bytes per minute for simplicity
    rx_rate = bytes_received / 60
    return tx_rate, rx_rate

def ping(host="8.8.8.8", count=4):
    print(f"Pinging {host} {count} times...")
    # In a real function, you'd use a system call to ping the host
    # This is just a placeholder for demonstration purposes
    return "Ping successful"


greet()  # Output: Hello, Network Engineer!

configure_interface("GigabitEthernet0/1", "192.168.1.1")

configure_interface(ip_address="192.168.1.1", interface_name="GigabitEthernet0/1")

tx, rx = calculate_metrics(3000, 5000)

print(f"Transmit Rate: {tx} Bps, Receive Rate: {rx} Bps")

print(ping())  # Uses default values

print(ping("192.168.1.1"))  # Overrides only the host

print(ping(count=8))  # Overrides only the count



