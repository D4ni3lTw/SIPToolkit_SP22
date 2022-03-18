import nmap
scanner = nmap.PortScanner()

def icmp_scan(ip):
    ip_addr=str(ip)
    scanner.scan('192.168.253.132', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state'])for x in scanner.all_hosts()]
    for host, status in hosts_list:
         print('{0}:{1}'.format(host, status))
    print(hosts_list)