from modules.initial import clear, welcome_screen
from modules.ultilities import term_size

def loadscreen():
    clear.clrscr()
    welcome_screen.banner('','',term_size.get_terminal_size("width"))

