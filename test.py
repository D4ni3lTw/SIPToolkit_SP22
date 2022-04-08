
result = {'default': {2: ('192.168.2.253', 'en0')}, 2: [('192.168.2.253', 'en0', True)], 30: [(
    'fe80::%utun0', 'utun0', False), ('fe80::%utun1', 'utun1', False), ('fe80::%utun2', 'utun2', False)]}
data = list(result.values())
data.pop(0)
list_card = []
for i in data:
    for j in i:
        # print(j)
        if(j[2] == True):
            list_card.append(j)
print(list_card)
