from secrets import choice
from tkinter import Menu
from bin.exploit import *
from bin.misc import *
from bin.report import *
from bin.scanning import *
from bin.vulnassesst import *
from py_console import console
from modules.ultilities import ip_valid
import sys


def continue_step(menu):
    choice = continue_menu()
    if choice == 1:
        main_flow(menu)
    if choice == 2:
        clear.clrscr()
        welcome_screen.banner('', '', term_size.get_terminal_size("width"))
        main_flow(print_menu())
    else:
        clear.clrscr()
        print('See you again!!!')


def main_flow(choice):
    default_username_list = 'data/wordlist/username.txt'
    default_password_list = 'data/wordlist/password.txt'
    default_username = 'hauhppse14'
    if (choice == 1):
        try:
            ip = str(input("Enter your IP address: ")).strip()
            validated_data = ip_valid.validator(ip)
            scandata = scanning(validated_data)
            vulndata = vulnassesst(ip, scandata)
            exploit(ip, default_username_list, default_password_list)
            report(scandata, vulndata, exploit)
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
            cpe = str(input("Enter cpe: "))
            # vulnassesst(ip, cpe)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 231):
        try:
            print('MITM attack with ARP poisoning')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 232):
        try:
            print('Flood DDOS attack')
            ip = str(input('Target IP: '))
            port = int(input('Port: '))
            duration = int(input('Number of seconds to send packets: '))
            exploit(ip, port, duration)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 233):
        try:
            print('Vishing')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 234):
        try:
            print('Identity(Username/Password) Bruteforce')
            ip = str(input('Target IP:'))
            usernames = str(input('Username wordlist:'))
            passwords = str(input('Password wordlist:'))
            bruteforce_login.bruteforcelogin(ip, usernames, passwords)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 235):
        try:
            print('Extension password cracking')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 236):
        try:
            print('SPIT attacks')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 237):
        try:
            print('Fuzzing')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 238):
        try:
            print('Misconfiguration and default passwords')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred!!!")
            sys.exit(1)

    if (choice == 239):
        try:
            print('Eavesdropping')
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
