import pandas as pd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import json


def get_vul_data():
    with open("reporting/vul_data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return [result['results'] if 'results' in result else [], result['total'] if 'total' in result else 0]


def get_scanning_data():
    with open("reporting/scan_data.json", 'r', encoding='UTF-8') as file:
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
        with open('report/' + today.strftime('%d' + '_%m_' + '%Y') +'/{0}.html'.format(ip_addr), 'w') as f:
            f.write(html)
