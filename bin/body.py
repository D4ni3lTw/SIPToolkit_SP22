from bin.exploit import *
from bin.misc import *
from bin.report import *
from bin.scanning import *
from bin.vulnassesst import *
from py_console import console
import sys


def main_flow(choice):
    if (choice == 1):
        try:
            ipaddr = choice("Enter your IP address: ")
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

    if (choice == 21):
        try:
            print('Enum_step')
            ip = str(input("Enter your IP address: "))
            scanning(str(ip))
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 22):
        try:
            print('VulAss_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 23):
        try:
            print('Exploit_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 24):
        try:
            print('Report_step')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 3):
        try:
            print('OPtions')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 4):
        try:
            print('go back')
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)