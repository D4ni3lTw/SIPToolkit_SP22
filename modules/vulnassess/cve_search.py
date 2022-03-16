import requests
import sys


def get_api(vendor, product):
    r = requests.get("https://cvepremium.circl.lu/api/search/%s/%s" %
                     (vendor, product))

    vulns = r.json()
    if vulns is not None:
        return vulns


def get_data(data):
    result = data['results']
    if result is not None:

        for v in result:
            vulnerable_configuration = v['vulnerable_configuration'][0]
            vulnerable_configuration_cpe_2_2 = v['vulnerable_configuration_cpe_2_2']
            vulnerable_product = v['vulnerable_product']
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

            print()
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







