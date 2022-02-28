from array import array
import nmap
nm=nmap.PortScanner()

print("_____TFTP-enumeration_____")
def Tftp_enum():#Scan target
    ip=input("Enter ip target:")
    ip_addr=str(ip)
    result=nm.scan(ip_addr,'69','-sU --script tftp-enum')
    return result

def getdata():# Get data from json result
    data=Tftp_enum()
    if data is None:
        print("No Data!!!")
    else:
        method=data['nmap']['scaninfo']['udp']['method']
        command_line=data['nmap']['command_line']
        port = data['nmap']['scaninfo']['udp']['services']
        state=data['scan']['192.168.50.145']['udp'][69]['state']
        service=data['scan']['192.168.50.145']['udp'][69]['name']
        file_enum=data['scan']['192.168.50.145']['udp'][69]['script']['tftp-enum']
        file_enum=file_enum.rstrip('\n')
        file_enum=file_enum.lstrip('\n')
        print("Command: ",command_line)
        print("\nPort is running at: ",port)
        print("State is: ",state)
        print("Service is running: ",service)
        print("List file:",file_enum)
getdata()

