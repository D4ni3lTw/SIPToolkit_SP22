import pandas as pd
from modules.reporter.utility import *

def scan_by_each_ip(ip_addr, scanning_data, vul_data, pentest_data, template, scanstats):
    info_by_port = scanning_data['scan'][str(ip_addr)]
    host_name = info_by_port['hostnames'][0]['name']
    os = info_by_port['osmatch'][0]['name']
    status = info_by_port['status']['state']
    if 'tcp' in info_by_port:
        tcp = info_by_port['tcp']
        table_tcp = tabling_data(
            list(tcp.keys()), tcp[list(tcp.keys())[0]], list(tcp.values()))
    else:
        table_tcp = None

    if 'udp' in info_by_port:
        udp = info_by_port['udp']
        table_udp = tabling_data(
            list(udp.keys()), udp[list(udp.keys())[0]], list(udp.values()))
    else:
        table_udp = None

    host_information = render_information("Host Information",
                                          render_body("Host name:", host_name) +
                                          render_body("IP Address:", ip_addr) +
                                          render_body("OS:", os) +
                                          render_body("Status:", status))
    port_scanning = render_information("Port Scanning:",
                                       render_body("TCP:", table_tcp.render()) if table_tcp != None else "" +
                                       render_body("UDP:", table_udp.render(
                                       )) if table_udp != None else "")

    vulerabilities = ''
    list_vul_data = sorted(vul_data,
                           key=lambda x: x['cvss'], reverse=True)
    critical_count = 0
    high_count = 0
    medium_count = 0
    low_count = 0
    for vul in list_vul_data:
        type = ''
        if(vul['cvss'] < 4):
            type = 'low'
            low_count += 1
        else:
            if(vul['cvss'] < 7):
                type = 'medium'
                medium_count += 1
            else:
                if (vul['cvss'] < 9):
                    type = 'high'
                    high_count += 1
                else:
                    type = 'critical'
                    critical_count += 1
        total = (critical_count, high_count, medium_count, low_count)
        vulerabilities = vulerabilities + \
            render_vulnerability(type, vul, total)
    rendered_pentest_data = ''
    for pentest in pentest_data:
        rendered_pentest_data += render_pentest(
            pentest['name'], pentest['value'])
    html = template.render(
        critical_count=critical_count,
        high_count=high_count,
        medium_count=medium_count,
        low_count=low_count,
        start_time=scanstats['timestr'],
        elapsed=scanstats['elapsed'],
        scanning_data=host_information+port_scanning,
        vul_data=vulerabilities,
        pentest_data=rendered_pentest_data
    )
    save_file(html, ip_addr)


def export(scanning_data, vul_data, pentest_data):
    template = get_template()
    scanstats = scanning_data['nmap']['scanstats']
    scanning = list(scanning_data['scan'].keys())
    for ip_addr in scanning:
        scan_by_each_ip(ip_addr, scanning_data, vul_data,
                        pentest_data, template, scanstats)
