import nmap

nm = nmap.PortScanner()
def service_scan(ip):
    ip_addr=str(ip)
    result=nm.scan(ip_addr,'0-5100','-O')
    #scanned_result = result['scan'].items()
    if result is not None:
        return result


