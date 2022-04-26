import platform
import time

if __name__ == '__main__':
    # Check Python version
    if platform.python_version() >= '3.0.0':
        print("\033[92mYour Python version is good to go!\033[0m")
    else:
        print("\033[91mYour version of Python is too old! \nPlease update to version 3\033[0m")
        sys.exit(1)

    # Check all Modules
    try:
        import sys
        import nmap
        import py_console
        import pyfiglet
        import PyInquirer
        import pyshark
        import pandas
        import jinja2
        import re
        print("\033[92mAll Modules is ready!\033[0m")
        time.sleep(1)
    except ModuleNotFoundError or ImportError:
        print("\033[1mYour system is missing required modules to run this program!!\n \033[92mpip install -r requirements.txt\033[0m \nOr try using these command to resolve the problem!!!\033[0m",
                "\n\033[93mpip install nmap \npip install py_console \npip install pyfiglet \npip install PyInquirer \npip install pyshark \npip install pandas \npip install re \npip install jinja2\033[0m")
        sys.exit(1)

    from bin.packet import *
    main()
