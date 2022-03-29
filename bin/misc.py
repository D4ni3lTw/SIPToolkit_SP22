import sys
from modules.initial import clear, welcome_screen
from modules.ultilities import module_checker, term_size
from PyInquirer import style_from_dict, prompt
from examples import custom_style_2

def loadscreen():
    clear.clrscr()
    module_checker.ensure_enviroment()
    welcome_screen.banner('','This is note',term_size.get_terminal_size("width"))

def main_choice():
    choice_prompt = {
        'type': 'list',
        'name': 'choice',
        'message': 'Please select choice suite your plan?',
        'choices': ['1. Run throught four step', '2. Run selected step', '3. Option', '4. Dung Chon Em', '5. Exit']
    }
    answers = prompt(choice_prompt, style=custom_style_2)
    return answers['choice']

def step_choice():
    step_prompt = {
        'type': 'list',
        'name': 'step',
        'message': 'Select a step to start the process!',
        'choices': ['1. Enumeration/Scanning', '2. Vulnerable Assessment', '3. Exploit', '4. Generate a Report', '5. Back to main menu']
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['step']

def pentest_choice():
    step_prompt = {
        'type': 'list',
        'name': 'pentest',
        'message': 'Select a pentesting process!',
        'choices': ['1. MITM attack with ARP poisoning',
                    '2. Flood DDOS attack',
                    '3. Vishing',
                    '4. Identity spoofing',
                    '5. Extension password cracking',
                    '6. SPIT attacks (send spam over VOIP networks)',
                    '7. Fuzzing',
                    '8. Misconfiguration and default passwords',
                    '9. Eavesdropping' ]
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['pentest']

def continue_choice():
    step_prompt = {
        'type': 'list',
        'name': 'rerun',
        'message': 'Do you want to continue ? (Y/N)',
        'choices': ['Yes', 'Continue with other steps', 'No']
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
    if (choose == '1. Run throught four step'):
        print("Run throught four step")
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
            if (pen_step == '1. MITM attack with ARP poisoning'):
                print("MITM attack")
                return 231
            elif (pen_step == '2. Flood DDOS attack'):
                print("Flood DDOS")
                return 232
            elif (pen_step == '3. Vishing'):
                print("Vishing")
                return 233
            elif (pen_step == '4. Identity spoofing'):
                print("Identity spoofing")
                return 234
            elif (pen_step == '5. Extension password cracking'):
                print("Extension password cracking")
                return 235
            elif (pen_step == '6. SPIT attacks (send spam over VOIP networks)'):
                print("SPIT attacks")
                return 236
            elif (pen_step == '7. Fuzzing'):
                print("Fuzzing")
                return 237
            elif (pen_step == '8. Misconfiguration and default passwords'):
                print("Misconfiguration and default passwords")
                return 238
            elif (pen_step == '9. Eavesdropping'):
                print("Eavesdropping")
                return 239

        elif (step == '4. Generate a Report'):
            print("Generate a Report")
            return 24
        elif (step == '5. Back to main menu'):
            clear.clrscr()
            welcome_screen.banner('','',term_size.get_terminal_size("width"))
            print_menu()

    elif (choose == '3. Option'):
        print("Do third choice")
        return 3

    elif (choose == '4. Dung Chon Em'):
        print("Hu qua")
        return 4

    elif (choose == '5. Exit'):
        clear.clrscr()
        print("See you again!!!")
        return 5
