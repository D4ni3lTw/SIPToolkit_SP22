from modules.scanner import *
from modules.scanner import portscanning

def scanning(ip):
    result = portscanning.service_scan(str(ip))
    print(result)
