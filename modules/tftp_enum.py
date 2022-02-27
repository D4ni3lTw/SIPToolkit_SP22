import nmap
nm=nmap.PortScanner()
def Tftp_enum():
    ip=input("Enter ip target:")
    ip_addr=str(ip)
    result=nm.scan(ip_addr,'69','-sU --script tftp-enum')
    return result
print('hello')