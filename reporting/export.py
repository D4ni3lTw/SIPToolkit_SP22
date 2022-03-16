import pandas as pd
from jinja2 import Environment, FileSystemLoader
import json


def get_data():
    with open("data.json", 'r', encoding='UTF-8') as file:
        result = json.loads(file.read())
        return [list(result.keys()), list(result.values())]


def get_template():
    env = Environment(loader=FileSystemLoader('templates'))
    return env.get_template('sample.html')


def tabling_data(index, data):
    df = pd.DataFrame(data, columns=['result'], index=index)
    return df.style


def save_file(html):
    with open('../report.html', 'w') as f:
        f.write(html)


[index, data] = get_data()
table = tabling_data(index, data)
template = get_template()
html = template.render(report_data=table.render())
save_file(html)
