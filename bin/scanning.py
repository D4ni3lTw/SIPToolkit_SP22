from modules.scanner import make_scan, get_sdata
from modules.initial import clear

def scanning(ip):
    clear.clrscr()
    print('Start Scanning!!')
    scan_data = make_scan.nmap_scan(ip, "1-500,5000-5500", "-v -sS -sV -sC -A -O -T5")
    if scan_data is not None:
        get_sdata.print_data_parse(ip, scan_data)
        return scan_data
    else:
        print("Something wrong with the scanner :((((")



