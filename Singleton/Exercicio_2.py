class ServerManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.servers = []
        return cls._instance

    def add_server(self, server_name):
        if server_name in self.servers:
            return False
        
        if server_name.startswith("http://") or server_name.startswith("https://"):
            self.servers.append(server_name)
            return True
        
        return False

    def get_http_servers(self):
        return [s for s in self.servers if s.startswith("http://")]

    def get_https_servers(self):
        return [s for s in self.servers if s.startswith("https://")]

if __name__ == "__main__":
    s1 = ServerManager()
    s2 = ServerManager()

    print(f"s1 é o mesmo objeto que s2? {s1 is s2}\n")

    print(f"Adicionando 'http://server1.com': {s1.add_server('http://server1.com')}")
    print(f"Adicionando 'https://server2.com': {s1.add_server('https://server2.com')}")
    print(f"Adicionando 'ftp://server3.com': {s2.add_server('ftp://server3.com')}")
    print(f"Adicionando 'http://server1.com': {s2.add_server('http://server1.com')}")
    print(f"Adicionando 'https://server4.com': {s1.add_server('https://server4.com')}")

    print("\nServidores HTTP:")
    print(s1.get_http_servers())

    print("\nServidores HTTPS:")
    print(s2.get_https_servers())

    print("\nLista completa (do s1):")
    print(s1.servers)