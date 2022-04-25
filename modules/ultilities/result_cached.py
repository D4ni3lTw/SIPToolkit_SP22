
import json
import os


def save_file_by_each_step(result, fileName):
    jsonString = json.dumps(result)
    path = f"result/{fileName}.json"
    if not os.path.exists('result/'):
        os.makedirs("result/",0o777)
    jsonFile = open(path, "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def get_file_by_each_step(fileName):
    path = f"result/{fileName}.json"
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            result = json.loads(file.read())
            return result
    except:
        return None
