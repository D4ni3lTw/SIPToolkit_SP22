from bin.exploit import *
from bin.misc import *
from bin.report import *
from bin.scanning import *
from bin.vulnassesst import *
from bin.body import *
from modules.ultilities import version_checker
from py_console import console
import sys



def main():
    # Check Python version
    if version_checker.checker() >= '3.0.0':
        print("\033[92mYour Python version is good to go!\033[0m")
    else:
        print("\033[91mYour version of Python is too old! \nPlease update to version 3\033[0m")
        sys.exit(1)
    # Starting Process
    # Check module before start
    # Run core
    try:
        loadscreen()
    except Exception as e:
        console.error("An Error Occurred!!!")
        console.error(e)
        sys.exit(1)
    except:
        console.error("Faill to start the program!!",
                      "\nPlease read the document for fearther information!!")
        sys.exit(1)

    # Main program function
    try:
        user_choice = print_menu()
        main_flow(user_choice)
    except Exception as e:
        console.error("An Error Occurred At Menu Interaction Step!!!")
        console.error(e)
        sys.exit(1)
    except:
        console.error("Faill to process correctly!!",
                      "\nPlease read the document for fearther information!!")
        sys.exit(1)