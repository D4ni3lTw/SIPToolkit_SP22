from bin.exploit import *
from bin.misc import *
from bin.report import *
from bin.scanning import *
from bin.vulnassesst import *
from py_console import console
import sys

def main():
    #Starting Process
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
    
    #Menu module 
    try:
        user_choice = print_menu()
    except Exception as e:
        console.error("An Error Occurred At Menu Interaction Step!!!")
        console.error(e)
        sys.exit(1)
    except:
        console.error("Faill to process correctly!!",
                    "\nPlease read the document for fearther information!!")
        sys.exit(1)

    #Main program function
    if (user_choice == 1):
        try:
            ipaddr = input("Enter your IP address: ")
            scanning(ipaddr)
            vulnassesst()
            exploit()
            report()
            console.success("Running cycle complete successfully!")
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)
    
    if (user_choice == 21):
        try:
            print('Enum_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)
    
    if (user_choice == 22):
        try:
            print('VulAss_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)
    
    if (user_choice == 23):
        try:
            print('Exploit_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (user_choice == 24):
        try:
            print('Report_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)
    
    if (user_choice == 3):
        try:
            print('OPtions')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (user_choice == 4):
        try:
            print('go back')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

