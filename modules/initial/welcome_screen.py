# import pyfiglet module
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("SIP Toolkit", font='larry3d')
    print(ascii_banner + "\033[1m\033[91m ~ By GSP22IA06\n\033[0m")
    # if note is not None:
    #     print(ascii_banner + str(note) +"\n\033[1m\033[91m ~ By GSP22IA06\n\033[0m")
    # else:
    #     print(ascii_banner + "\033[1m\033[91m ~ By GSP22IA06\n\033[0m")