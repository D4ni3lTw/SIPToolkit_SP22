import csv
from cvss import CVSS2, CVSS3

vector = 'CVSS:3.0/S:C/C:N/I:N/A:N/AV:P/AC:H/PR:H/UI:N/E:H/RL:O/RC:R/CR:H/IR:X/AR:X/MAC:H/MPR:X/MUI:R/MC:H/MA:N'
c = CVSS3(vector)
cal = c.scores()
print(cal)
print(type(cal))


def sosanh(a:float):
    if a <=0.0:
        return "None"
    elif a >=0.1 and a <=3.9:
        return "Low"
    elif a >=4.0 and a<=6.9:
        return "Medium"
    elif a>=7.0 and a<=8.9:
        return "High"
    elif a>=9.0 and a<=10.0:
        return "Critical"
    else:
        return "Nothing"


cvs = dict()
cvslist=list()

for a in cal:
    score = float(a)
    cvslist.append(sosanh(score))

cvs['base_metric']=cvslist[0]
cvs['temporal_metric']=cvslist[1]
cvs['environment_metric']=cvslist[2]


print("Basemetric:",cvs["base_metric"])
print("Tempmetric:",cvs["temporal_metric"])
print("Environtmetric:",cvs["environment_metric"])


    



 







