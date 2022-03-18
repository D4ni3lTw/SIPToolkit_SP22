import pandas as pd
from jinja2 import Environment, FileSystemLoader
import json
import nmap


def get_data():
    with open("reporting/data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return [list(result.keys()), list(result.values())]


def get_info():
    with open("reporting/data3.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return result
    scanner = nmap.PortScanner()
    ip_addr = "172.16.0.115"
    data = scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    return data


def get_template():
    env = Environment(loader=FileSystemLoader('reporting/templates'))
    return env.get_template('sample.html')


def tabling_data(index, columns, data):
    df = pd.DataFrame(data, columns=columns, index=index)
    return df.style


def render_vulnerability_title(type, name):
    result = '<div class="vulnerability {0}">{1}</div>'.format(type, name)
    return result


def render_information(header, body):
    result = '<div><p class="title">{0}</p><hr class="solid">{1}</div>'.format(
        header, body)
    return result


def render_body(title, content):
    result = '<p>{0}: <span class="content">{1}</span></p>'.format(
        title, content)
    return result


def save_file(html):
    with open('report.html', 'w') as f:
        f.write(html)


[index, data] = get_data()
pentest_info = get_info()
template = get_template()
scanstats = pentest_info['nmap']['scanstats']
scanning = list(pentest_info['scan'].keys())

for ip_addr in scanning:
    info_by_port = pentest_info['scan'][ip_addr]
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
                                          render_body("Host name", host_name) +
                                          render_body("IP Address", ip_addr) +
                                          render_body("OS", os) +
                                          render_body("Status", status))
    port_scanning = render_information("Port Scanning",
                                       render_body("TCP", table_tcp.render()) if table_tcp != None else "" +
                                       render_body("UDP", table_udp.render(
                                       )) if table_udp != None else "")
    html = template.render(
        start_time=scanstats['timestr'],
        elapsed=scanstats['elapsed'],
        general_info=host_information+port_scanning
    )

save_file(html)
