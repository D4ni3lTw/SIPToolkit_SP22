import requests
import sys
import json

def get_vul_data(ip, data):
    scan_data = data['scan']
    dict_cpe = get_cpe_dictionary()
    if scan_data is not None:
        list_vul = []
        if 'tcp' in scan_data[str(ip)]:
            tcp = scan_data[str(ip)]['tcp']
            portlist = list(tcp.keys())
            for port in portlist:
                port_num = port
                port_cpe = tcp[port]['cpe']
                port_cpe = 'cpe:/a:freeswitch:freeswitch:1.10.6' if (
                    port_cpe == '' and tcp[port]['product'] == 'FreeSWITCH') else port_cpe
                if port_cpe != '':
                    cpe_arr = port_cpe.split(':')
                    cpe_arr.remove('cpe')
                    cpe_arr.remove('/a')
                    cpe_arr.pop(0)
                    cpe_rejoin = ':'.join(cpe_arr)
                    for cpe_item in dict_cpe:
                        if(cpe_rejoin in cpe_item):
                            list_full_vul_data = get_api(cpe_item)
                            for vul in list_full_vul_data:
                                if type(vul) is dict:
                                    if('vulnerable_configuration' in vul):
                                        del vul['vulnerable_configuration']
                                    if('vulnerable_product' in vul):
                                        del vul['vulnerable_product']
                                    if('vulnerable_configuration_cpe_2_2' in vul):
                                        del vul['vulnerable_configuration_cpe_2_2']
                                    list_vul.append(vul)
                            break
        return list_vul


def get_cpe_dictionary():
    with open("data/cpe_dictionary/data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return result


def get_api(cpe):
    r = requests.get("https://cvepremium.circl.lu/api/cvefor/%s" % (cpe))
    vulns = r.json()
    if (vulns is not None):
        return vulns


def print_data(result):
    if result is not None:
        for v in result:
            Modified = v['Modified']
            Published = v['Published']

            # Access
            authentication = v['access']['authentication']
            complexity = v['access']['complexity']
            vector = v['access']['vector']

            assigner = v['assigner'][0]
            capec = v['assigner']
            cvss = v['cvss']
            impactScore = v['impactScore']
            exploitabilityScore = v['exploitabilityScore']
            cvss_time = v['cvss-time']
            cvss_vector = v['cvss-vector']
            cwe = v['cwe']
            cveid = v['id']

            # impact
            availability = v['impact']['availability']
            confidentiality = v['impact']['confidentiality']
            integrity = v['impact']['integrity']

            # impact3
            availability3 = v['impact3']['availability']
            confidentiality3 = v['impact3']['confidentiality']
            integrity3 = v['impact3']['integrity']

            # exploitability3
            attackvector = v['exploitability3']['attackvector']
            attackcomplexity = v['exploitability3']['attackcomplexity']
            privilegesrequired = v['exploitability3']['privilegesrequired']
            userinteraction = v['exploitability3']['userinteraction']
            scope = v['exploitability3']['scope']

            cvss3 = v['cvss3']
            impactScore3 = v['impactScore3']
            exploitabilityScore3 = v['exploitabilityScore3']
            cvss3_vector = v['cvss3-vector']
            last_modified = v['last-modified']

            for references in v['references']:
                ref = references

            summary = v['summary']
            print("=============== " + cveid + " ===============")
            print(" CWE: ", cwe)
            print(" CVSS: ", cvss)
            print(" Impact Score: ", impactScore)
            print(" Exploitability Score: ", exploitabilityScore)
            print(" Impact: ", availability, confidentiality, integrity)
            print(" Impact 3: ", availability3, confidentiality3, integrity3)
            print(" CVSS3: ", cvss3)
            print(" Impact Score 3: ", impactScore3)
            print(" Exploitability Score 3: ", exploitabilityScore3)
            print(" Summary: ", summary)
            print()

