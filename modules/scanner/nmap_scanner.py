import nmap

scanner = nmap.PortScanner()

def syn_ack_scan(ip_addr):
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def udp_scan(ip_addr):
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

def comprehensive_scan(ip_addr):
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def regular_scan(ip_addr):
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def os_detect(ip_addr):
    print(scanner.scan(ip_addr, arguments="-O")
          ['scan']['127.0.0.1']['osmatch'][1])

def multi_scan(ip_addr):
    ip_addr = input()
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def icmp_scan(ip_addr):
    scanner.scan(hosts=ip_addr,
                 arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state'])
                  for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

ip_addr = input('Enter IP Address: ')
icmp_scan(ip_addr)
syn_ack_scan(ip_addr)
udp_scan(ip_addr)
comprehensive_scan(ip_addr)
regular_scan(ip_addr)
os_detect(ip_addr)
multi_scan(ip_addr)


