import sys
from PyInquirer import style_from_dict, prompt
from examples import custom_style_2
def main_choice():
    choice_prompt = {
        'type': 'list',
        'name': 'choice',
        'message': 'Please select choice suite your plan?',
        'choices': ['1. Run throught four step', '2. Run selected step', '3. Option', '4. Dung Chon Em']
    }
    answers = prompt(choice_prompt, style=custom_style_2)
    return answers['choice']

def step_choice():
    step_prompt = {
        'type': 'list',
        'name': 'step',
        'message': 'Select a step to start the process!',
        'choices': ['1. Enumeration/Scanning', '2. Vulnerable Assessment', '3. Exploit', '4. Generate a Report']
    }
    answers = prompt(step_prompt, style=custom_style_2)
    return answers['step']

def menu():
    menu_info = ("\x1B[3mThis tool is design to be capable of help pentester with these main step:\x1B[0m\n"
            "-Enumeration/ Scanning\n"
            "-Vulnerable assessment\n"
            "-Exploit\n"
            "-Generate a report\n")
    print(menu_info)
    choose = main_choice()
    if (choose == '1. Run throught four step'):
        print("Do first choice")
    
    elif (choose == '2. Run selected step'):
        step = step_choice()
        if (step == '1. Enumeration/Scanning'):
            print("Enum")
        elif (step == '2. Vulnerable Assessment'):
            print("Vulnerable Assessment")
        elif (step == '3. Exploit'):
            print("Exploit")
        elif (step == '4. Generate a Report'):
            print("Generate a Report")

    elif (choose == '3. Option'):
        print("Do third choice")

    elif (choose == '4. Dung Chon Em'):
        print("Hu qua")


if __name__ == "__main__":
    print_menu()
