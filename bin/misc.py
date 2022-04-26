import sys
from modules.initial import clear, welcome_screen
from modules.ultilities import term_size
from PyInquirer import style_from_dict, prompt
from examples import custom_style_2

def loadscreen():
    clear.clrscr()
    welcome_screen.banner('','This is note',term_size.get_terminal_size("width"))

def main_choice():
    choice_prompt = {
        'type': 'list',
        'name': 'choice',
        'message': 'Please select choice suite your plan?',
        'choices': [
            '1. Run through four step',
            '2. Run selected step',
            '3. Exit']
    }
    answers = prompt(choice_prompt, style=custom_style_2)
    return answers['choice']

def step_choice():
    step_prompt = {
        'type': 'list',
        'name': 'step',
        'message': 'Select a step to start the process!',
        'choices': [
            '1. Enumeration/Scanning',
            '2. Vulnerable Assessment',
            '3. Exploit',
            '4. Generate a Report',
            '5. Back to main menu'
        ]
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['step']

def pentest_choice():
    step_prompt = {
        'type': 'list',
        'name': 'pentest',
        'message': 'Select a pentesting process!',
        'choices': ['1. Flood DDOS attack',
                    '2. Bruteforce SSH',
                    '3. Bruteforce Login (Support CSRF bypass)',
                    '4. Fuzzing',
                    '5. Extension password cracking',
                    '6. Eavesdropping' ]
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['pentest']

def continue_choice():
    step_prompt = {
        'type': 'list',
        'name': 'rerun',
        'message': 'Do you want to continue ? (Y/N)',
        'choices': [
            'Yes',
            'Continue with other steps',
            'No']
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['rerun']

def continue_menu():
    choose = continue_choice()
    if (choose == 'Yes'):
        return 1
    elif (choose == 'Continue with other steps'):
        return 2
    elif (choose == 'No'):
        return 3

def print_menu():
    #Menu description
    menu = ("\x1B[3mThis tool is design to be capable of help pentester with these main step:\x1B[0m\n"
            "-Enumeration/ Scanning\n"
            "-Vulnerable assessment\n"
            "-Exploit\n"
            "-Generate a report\n")
    print(menu)
    #Menu main step
    choose = main_choice()
    if (choose == '1. Run through four step'):
        print("Run through four step")
        return 1

    #Menu selected step
    elif (choose == '2. Run selected step'):
        step = step_choice()
        if (step == '1. Enumeration/Scanning'):
            print("Enumeration")
            return 21
        elif (step == '2. Vulnerable Assessment'):
            print("Vulnerable Assessment")
            return 22

        #Menu pentesting step
        elif (step == '3. Exploit'):
            pen_step = pentest_choice()
            if (pen_step == '1. Flood DDOS attack'):
                print("Flood DDOS")
                return 231
            elif (pen_step == '2. Bruteforce SSH'):
                print("Bruteforce SSH")
                return 232
            elif (pen_step == '3. Bruteforce Login (Support CSRF bypass)'):
                print("Bruteforce Login")
                return 233
            elif (pen_step == '4. Directory Fuzzing'):
                print("Identity(Username/Password) Brute-force")
                return 232
            elif (pen_step == '3. Extension password cracking'):
                print("Extension password cracking")
                return 235
            elif (pen_step == '6. Eavesdropping'):
                print("Eavesdropping")
                return 236

        elif (step == '4. Generate a Report'):
            print("Generate a Report")
            return 24
        elif (step == '5. Back to main menu'):
            clear.clrscr()
            welcome_screen.banner('','',term_size.get_terminal_size("width"))
            print_menu()

    elif (choose == '3. Exit'):
        clear.clrscr()
        print("See you again!!!")
        return 3
