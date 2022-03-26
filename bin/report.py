from modules.reporter.export import *


def report(scanning_data, vul_data, pentest_data=""):
    if scanning_data != None and vul_data != None:
        export(scanning_data, vul_data, pentest_data)
