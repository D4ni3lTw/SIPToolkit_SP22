import pandas as pd
from jinja2 import Environment, FileSystemLoader
from modules.reporter.utility import *


def render_vulnerability(vul, total):
    result = render_vulnerability_header(
        "general", vul['id'] + ' | ' + vul['cwe'])
    vul_conf = convert_array_data(vul['vulnerable_configuration'])
    result += render_information("Vulnerable Configuration",
                                 render_body(vul_conf, ""))
    result += render_information("Modified", render_body(vul['Modified'], ""))
    result += render_information("Published",
                                 render_body(vul['Published'], ""))
    result += render_information("Assigner", render_body(vul['assigner'], ""))

    result += render_information("CVSS v2.0 Score", render_body(
        "{0} ({1})".format(str(vul['cvss']), vul['cvss-vector']), ""))
    result += render_information("CVSS v3.0 Score", render_body(
        "{0} ({1})".format(str(vul['cvss3']), vul['cvss3-vector']), ""))
    ref = convert_array_data(vul['references'])
    result += render_information("References", render_body(ref, ""))
    result += render_information("Summary", render_body(vul['summary'], ""))

    return result


def scan_by_each_ip(ip_addr, scanning_data, vul_data, pentest_data, template, scanstats):
    info_by_port = scanning_data['scan'][ip_addr]
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

    # [vul_data, total_vul_data] = get_vul_data()
    vulerabilities = ''
    for vul in vul_data['results']:
        vulerabilities = vulerabilities + \
            render_vulnerability(vul, vul_data['total'])

    html = template.render(
        count=vul_data['total'],
        start_time=scanstats['timestr'],
        elapsed=scanstats['elapsed'],
        scanning_data=host_information+port_scanning,
        vul_data=vulerabilities
    )
    save_file(html, ip_addr)


def export(scanning_data, vul_data, pentest_data):
    # scanning_data = get_scanning_data()
    template = get_template()
    scanstats = scanning_data['nmap']['scanstats']
    scanning = list(scanning_data['scan'].keys())
    for ip_addr in scanning:
        scan_by_each_ip(ip_addr, scanning_data, vul_data,
                        pentest_data, template, scanstats)
