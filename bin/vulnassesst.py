from modules.vulnassess import cve_search
def vulnassesst(ips, scan_data):
    vul_data = cve_search.get_vul_data(ips, scan_data)    
    cve_search.print_data(vul_data)
    return vul_data