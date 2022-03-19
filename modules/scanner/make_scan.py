import nmap

scanner = nmap.PortScanner()

def nmap_scan(ip, ports, arguments):
    ip_addr=str(ip)
    data = scanner.scan(ip_addr, ports, arguments)
    if data is not None:
        return data
    else:
        return -1

