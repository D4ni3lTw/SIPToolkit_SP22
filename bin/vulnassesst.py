from modules.vulnassess import cve_search

def vulnassesst(vendor,product):
    api = cve_search.get_api(vendor, product)
    cve_search.get_data(api)