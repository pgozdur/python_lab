class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
    
    def display_config(self):
        print(f"Hostname: {self.hostname}, IP Address: {self.ip_address}")
    

class Router(NetworkDevice):
    def __init__(self, hostname, ip_address,routing_protocol):
        super().__init__(hostname, ip_address)
        self.routing_protocol = routing_protocol

    def display_config(self):
        super().display_config()
        print(f"Routing Protocol: {self.routing_protocol}")


router = NetworkDevice("Router1", "192.168.1.1")
router2= NetworkDevice("Router2", "11.1.1.1")


pawel = [1,2,3]
print(type(pawel))
pawel.append(4)


# router.display_config()

nowy_obiekt = Router("Router1", "192.168.1.1","OSPF")
nowy_obiekt.display_config()
print(f"Routing Protocol: {nowy_obiekt.routing_protocol}")

# When you create an instance of the class and call a method, 
# Python automatically passes the instance as the first argument. 
# So when you call router.display_config(), Python is actually calling NetworkDevice.display_config(router).

