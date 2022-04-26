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
import time


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
    default_fuzzing_list = 'data/wordlist/sample_dir.txt'
    if (choice == 1):
        try:
            ip = str(input("Enter your IP address: ")).strip()
            if (ip_valid.validator(ip)):
                scandata = scanning(ip)
                vul_data = vulnassesst(ip, scandata)
                print('------------------------------------------------')
                input("Press Enter to continue to Pentest phase...")
                pentest_data = exploit( ip, default_username_list, default_password_list, default_fuzzing_list)
                print(pentest_data)
                report(scandata, vul_data, pentest_data)
                console.success("Running cycle complete successfully!")
                continue_step(choice)
            else:
                console.error("Incorrect IP format!!!")
                pass
        except Exception as e:
            console.error("An Error Occurred At Automatic Step!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Automatic Step!!!")
            sys.exit(1)

    if (choice == 21):
        try:
            ip = input("Enter your IP address: ")
            ip = ip.rstrip('\n')
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
            print('Search vulnerability related to Common Platform Enumeration (CPE)')
            print('CPE Format: cpe:/a:<vendor>:<product>:<version>')
            cpe = str(input("Enter cpe: "))
            ip = '0.0.0.0'
            vulnassesst(ip, scan_data=None, port_cpe=cpe)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Vulnerability Assessment!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Vulnerability Assessment!!!")
            sys.exit(1)

    if (choice == 231):
        try:
            ip = str(input('Target IP: '))
            port = int(input('Port: '))
            duration = int(input('Number of seconds to send packets: '))
            floodddos(ip, port, duration)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Flood DDOS!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Flood DDOS!!!")
            sys.exit(1)

    if (choice == 232):
        try:
            ip = str(input('Target IP: '))
            default_username_list = str(input('Username Wordlist: '))
            default_password_list = str(input('Password Wordlist: '))
            bruteforce_ssh.bruteforce(ip, default_username_list, default_password_list)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Bruteforce SSH!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Bruteforce SSH!!!")
            sys.exit(1)

    if (choice == 233):
        try:
            ip = str(input('Target IP:'))
            usernames = str(input('Username wordlist:'))
            passwords = str(input('Password wordlist:'))
            bruteforce_login.bruteforcelogin(ip, usernames, passwords)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Bruteforce Login!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Bruteforce Login!!!")
            sys.exit(1)


    if (choice == 234):
        try:
            url = str(input('Target URL:'))
            fuzzing_list = str(input('Fuzzing Wordlist: '))
            fuzzing.dir_fuzzing(url, fuzzing_list, showRedirect=None)
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Directory Fuzzing!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Directory Fuzzing!!!")
            sys.exit(1)

    if (choice == 233):
        try:
            # print('Vishing')
            print('Extension password cracking')
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
            # print('Identity(Username/Password) Bruteforce')
            # ip = str(input('Target IP:'))
            # usernames = str(input('Username wordlist:'))
            # passwords = str(input('Password wordlist:'))
            # bruteforce_login.bruteforcelogin(ip, usernames, passwords)
            print('Fuzzing')
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
            # print('Extension password cracking')
            print('Eavesdropping')
            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Extension Password Cracking!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Extension Password Cracking!!!")
            sys.exit(1)

    if (choice == 236):
        try:
            filename = str(input('Output Filename: '))
            eaves_timeout = int(input('Eavesdropping timeout: '))
            if filename != '' or eaves_timeout != '':
                eavesdrop.eavesdropping(str(filename), eaves_timeout)
            else:
                print('[-] Empty Output Filename or Eavesdropping timeout')

            continue_step(choice)
        except Exception as e:
            console.error("An Error Occurred At Manual Eavesdropping!!!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred At Manual Eavesdropping!!!")
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
        pass
