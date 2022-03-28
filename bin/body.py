from secrets import choice
from tkinter import Menu
from bin.exploit import *
from bin.misc import *
from bin.report import *
from bin.scanning import *
from bin.vulnassesst import *
from py_console import console
import sys

def continue_step(menu):
    choice = continue_menu()
    if choice == 1:
        main_flow(menu)
    if choice == 2:
        clear.clrscr()
        welcome_screen.banner('','',term_size.get_terminal_size("width"))
        main_flow(print_menu())
    else:
        clear.clrscr()
        print('See you again!!!')

def main_flow(choice):
    if (choice == 1):
        try:
            ip = str(input("Enter your IP address: "))
            scandata = scanning(str(ip))
            vulndata = vulnassesst('signalwire', 'freeswitch')
            exploit()
            report(scandata,vulndata)
            console.success("Running cycle complete successfully!")
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 21):
        try:
            ip = str(input("Enter your IP address: "))
            scanning(str(ip))
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 22):
        try:
            vendor = str(input("Enter vendor: "))
            product = str(input("Enter product: "))
            vulnassesst(vendor,product)
            continue_step(choice)
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
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 24):
        try:
            report("/t")
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 3):
        try:
            print('Options')
            continue_step(choice)
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
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 5):
        pass
