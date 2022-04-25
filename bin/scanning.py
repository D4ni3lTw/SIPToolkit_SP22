from modules.ultilities.result_cached import save_file_by_each_step, get_file_by_each_step
from modules.reporter.utility import save_file
from modules.scanner import make_scan, get_sdata
from modules.initial import clear
def scanning(ip):
    clear.clrscr()
    print('Start Scanning!!')
    scan_data = get_file_by_each_step('scan_data')
    if scan_data is None:   
        scan_data = make_scan.nmap_scan(ip, "1-500,5000-5500", "-v -sS -sV -sC -A -O -T5")
    if scan_data is not None:
        get_sdata.print_data_parse(ip, scan_data)
        save_file_by_each_step(scan_data,'scan_data')
        return scan_data
    else:
        print("Something wrong with the scanner :((((")
        return None



