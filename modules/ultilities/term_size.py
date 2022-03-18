import os

def get_terminal_size(input):
    columns, rows = os.get_terminal_size()
    if input == 'width':
        return columns
    elif input == 'height':
        return rows
    else:
        return columns, rows
