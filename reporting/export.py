import pandas as pd
from jinja2 import Environment, FileSystemLoader
import json


def get_data():
    with open("reporting/data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return [list(result.keys()), list(result.values())]


def get_info():
    with open("reporting/data2.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return result


def get_template():
    env = Environment(loader=FileSystemLoader('reporting/templates'))
    return env.get_template('sample.html')


def tabling_data(index, data):
    df = pd.DataFrame(data, columns=['result'], index=index)
    return df.style


def render_vulnerability_title(type, name):
    result = '<div class="vulnerability {0}">{1}</div>'.format(type, name)
    return result


def render_vulnerability_content(title, content):
    result = '<p class="title">{0}</p><hr class="solid"> <p>{1}</p>'.format(
        title, content)
    return result


def save_file(html):
    with open('report.html', 'w') as f:
        f.write(html)


[index, data] = get_data()
pentest_info = get_info()
name_1 = render_vulnerability_title("critical", "vul01")
table = tabling_data(index, data)
template = get_template()
# html = template.render(report_data=table.render(),
#                        )
html = template.render(
    ip_addr=pentest_info['ip_addr'],
    start_time=pentest_info['start_time'],
    end_time=pentest_info['end_time'],
    os_info=pentest_info['os_info'],
    data=name_1,
)
save_file(html)
