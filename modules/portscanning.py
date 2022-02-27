import nmap

nm = nmap.PortScanner()
def service_scan():
    ip=input("Enter ip: ")
    ip_addr=str(ip)
    result=nm.scan(ip_addr,'20-5100','-sV')
    return result

def getdata():
    data = service_scan()
    if data is None:
        print("No data")
    else
        port22_name = data['scan']['3.0.94.34']['tcp'][22]['name']
        port22_ver = data['scan']['3.0.94.34']['tcp'][22]['version']
        port80_name = data['scan']['3.0.94.34']['tcp'][80]['name']
        port80_ver = data['scan']['3.0.94.34']['tcp'][80]['version']
        port443_name = data['scan']['3.0.94.34']['tcp'][443]['name']
        port443_ver = data['scan']['3.0.94.34']['tcp'][443]['version']
        port5060_name = data['scan']['3.0.94.34']['tcp'][5060]['name']
        port5060_ver = data['scan']['3.0.94.34']['tcp'][5060]['version']
        port5080_name = data['scan']['3.0.94.34']['tcp'][5080]['name']
        port5080_ver = data['scan']['3.0.94.34']['tcp'][5080]['version']
        print("Name: ", port22_name)
        print("Version: ", port22_ver)
        print("Name: ", port80_name)
        print("Version: ", port80_ver)
        print("Name: ", port443_name)
        print("Version: ", port443_ver)
        print("Name: ", port5060_name)
        print("Version: ", port5060_ver)
        print("Name: ", port5080_name)
        print("Version: ", port5080_ver)

getdata()