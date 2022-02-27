import nmap as m

scanner = m.PortScanner()

ip = input("Enter IP address: ")
ip_addr = str(ip)
response = print("""\nPlease enter the type of scan you want to run
                1. Port Scan
                2. UDP Scan
                3. Service Scan
                4. Regular Scan
                5. OS Detection
                6. Multiple IP inputs
                7. Ping Scan\n""")
response = input("You have selected option: ")

# If user's input is 1, perform a SYN/ACK scan
if response == '1':
    print("Nmap Version: ", scanner.nmap_version())
    # Here, v is used for verbose, which means if selected it will give extra information
    # 1-1024 means the port number we want to search on
    # -sS means perform a TCP SYN connect scan, it send the SYN packets to the host
    scanner.scan(ip_addr, '1-6000', '-v -sS')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

# If user's input is 2, perform a UDP Scan
elif response == '2':
    # Here, v is used for verbose, which means if selected it will give #extra information
    # 1-1024 means the port number we want to search on
    # -sU means perform a UDP SYN connect scan, it send the SYN packets to #the host
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '5060', '-v -sU')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

# If user's input is 3, perform a Comprehensive scan
elif response == '3':
    print("Nmap Version: ", scanner.nmap_version())
    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS
    scanner.scan(ip_addr, '1-6000', '-sV')


# If user's input is 4, perform a Regular Scan
elif response == '4':
    # Works on default arguments
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

#127.0.0.1 thì ra còn 3.0.94.34 thì out of range
elif response == '5':
    print(scanner.scan('3.0.94.34', arguments="-O")['scan']['3.0.94.34']['osmatch'][1])

elif response == '6':
    print("Nmap Version: ", scanner.nmap_version())
    # Here, v is used for verbose, which means if selected it will give extra information
    # 1-1024 means the port number we want to search on
    # -sS means perform a TCP SYN connect scan, it send the SYN packets to the host
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif response == '7':
    scanner.scan(hosts=ip_addr, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

else:
    print("Please choose a number from the options above")


