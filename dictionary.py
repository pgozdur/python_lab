device = {
    "hostname": "Router1",
    "ip": "192.168.1.1",
    "model": "Cisco 2901",
    "interfaces": ["GigabitEthernet0", "GigabitEthernet1"]
}
print(device)


ip_address = device["ip"]
print(f"Device IP Address: {ip_address}")

device["location"] = "Data Center A"
print(device)

device["ip"] = "192.168.2.1"
print(device)

del device["model"]  # Using del
location = device.pop("location")  # Using pop, also retrieves the value

print(device)

lista_kluczy = []
for key in device.keys():
    lista_kluczy.append(key)

lista_wartosci = []
for value in device.values():
    lista_wartosci.append(value)


print(lista_kluczy)
print(lista_wartosci)

print("##########################")

for key, value in device.items():
    print(f"{key}: {value}")


