import re

regex = '^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'

def ip_spliter(ips):
    if ' ' in ips:
        ip = ips.split(' ')
        return ip
    else:
        return [ips]

def listconverter(list):
    init_str = " "
    return (init_str.join(list))

def validator(input):
    validated = []
    ips = ip_spliter(input)
    for valid_ip in ips:
        if(re.search(regex, valid_ip)):
            validated.append(valid_ip)
        else:
            pass
    return listconverter(validated)
