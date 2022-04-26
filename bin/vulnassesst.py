from modules.ultilities.result_cached import save_file_by_each_step, get_file_by_each_step
from modules.vulnassess import cve_search


def vulnassesst(ip, scan_data, port_cpe=None):
    print('\n----------------------------------------------------')
    print('Vulnerability Assessment')
    print('----------------------------------------------------')
    vul_data = get_file_by_each_step('vul_data', ip)
    if vul_data is None:
        vul_data = cve_search.get_vul_data(ip, scan_data, port_cpe)
        print(vul_data)
    if vul_data is not None:
        cve_search.print_data(vul_data)
        save_file_by_each_step(vul_data, 'vul_data', ip)
        return vul_data
    elif vul_data is None and port_cpe is not None:
        vul_data = cve_search.get_vul_data(ip, scan_data, port_cpe)
        if vul_data != []:
            cve_search.print_data(vul_data)
        else:
            print('[-] No Vulnerability data found for this CPE\n')
    else:
        print("[-] Something wrong when getting vulnerabilities")
        return None
