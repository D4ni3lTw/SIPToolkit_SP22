import pandas as pd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import json


def render_vulnerability(type, vul, total):
    result = render_vulnerability_header(
        type, vul['id'] + ' | ' + vul['cwe'])
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


def render_pentest(name, value):
    result = render_information(name,
                                render_body('Username', value['username'] +
                                            render_body('Password', value['password'])))
    return result


def get_vul_data():
    with open("modules/reporter/vul_data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return result


def get_scanning_data():
    with open("modules/reporter/scan_data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return result


def get_template():
    env = Environment(loader=FileSystemLoader('data/report_templates'))
    return env.get_template('sample.html')


def tabling_data(index, columns, data):
    df = pd.DataFrame(data, columns=columns, index=index)
    return df.style


def render_vulnerability_header(type, name):
    result = '<div class="vulnerability {0}">{1}</div>'.format(type, name)
    return result


def render_information(header, body):
    result = '<div><p class="title">{0}</p><hr class="solid">{1}</div>'.format(
        header, body)
    return result


def render_body(title, content):
    result = '<p>{0} <span class="content">{1}</span></p>'.format(
        title, content)
    return result


def convert_array_data(array):
    ref = ''
    for i in array:
        ref += render_body(i, "")
    return ref


def save_file(html, ip_addr):
    today = datetime.now()
    if not os.path.exists('report/' + today.strftime('%d' + '_%m_' + '%Y')):
        os.makedirs("report/" + today.strftime('%d' + '_%m_' + '%Y'))
        with open('report/' + today.strftime('%d' + '_%m_' + '%Y') + '/{0}.html'.format(ip_addr), 'w') as f:
            f.write(html)
