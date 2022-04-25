
import json
import os


def save_file_by_each_step(result, fileName, ip):
    jsonString = json.dumps(result)
    path = f'result/{ip}/'
    if not os.path.exists(path):
        os.makedirs(path, 0o777)
    jsonFile = open(f'{path}{fileName}.json', 'w')
    jsonFile.write(jsonString)
    jsonFile.close()


def get_file_by_each_step(fileName, ip):
    path = f'result/{ip}/{fileName}.json'
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            result = json.loads(file.read())
            return result
    except:
        return None
