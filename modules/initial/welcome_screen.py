# import pyfiglet module
import pyfiglet

def banner(title = 'SIP Toolkit', description = '', columns = 100):
    if (title == '') or (description == '') or (columns == '') or ( title == '' and description == '') :
        ascii_banner = pyfiglet.figlet_format('SIP Toolkit: A Telephony Pentest Tool', font='larry3d', width = int(columns))
        print(ascii_banner + "\n\033[1m\033[91m ~ By GSP22IA06\n\033[0m")
    else:
        ascii_banner = pyfiglet.figlet_format(title, font='larry3d', width = int(columns))
        print(ascii_banner + "\n" + description + "\n\033[1m\033[91m ~ By GSP22IA06\n\033[0m")

