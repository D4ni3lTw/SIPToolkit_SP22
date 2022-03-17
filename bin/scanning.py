from modules.scanner import nmap_scan, get_data
from modules.initial import clear

def scanning(ipaddr):
    if ' ' in ipaddr:
        ips = ipaddr.split(' ')
        clear.clrscr()
        for ip in ips:
            # ICMP Ping
            print("\nScanned IP: " + ip)
            print('1. Test ICMP ARP ping')
            report = nmap_scan.do_scan(str(ip), "-sP -PP -PR -T5")
            if report:
                get_data.icmp_sweep(report, ip)
            else:
                print("No results returned")

            # TCP ACK Ping
            print('2. Test TCP ACK pings')
            report2 = nmap_scan.do_scan(str(ip), "-sP -PE -T5")
            if report2:
                get_data.icmp_sweep(report2, ip)
            else:
                print("No results returned")

            #UDP Ping
            print('3. Test UDP Ping')
            report3 = nmap_scan.do_scan(str(ip), "-sP -PU -T5")
            if report3:
                get_data.icmp_sweep(report3, ip)
            else:
                print("No results returned")

            #Port / Service scanning
            print('4. Port Scanning')
            report4 = nmap_scan.do_scan(str(ip), "-p0-10000 -sV -sC -T5")
            if report4:
                get_data.port_scanning(report4)
            else:
                print("No results returned")



