

db=['ssh', 'OpenSSH', '7.4', 'http', 'nginx', '1.20.1', 'sip', 'FreeSWITCH']

def searchsploit():
    check = True
    while check == True:
        search=input("Search vulnerability:")
        if search in db:
            if search == "sip" or search == "SIP" or search == "FreeSWITCH":
                print("---------------------------------------------------------------------------------------")
                print("Vulnerabe VOIP Title                      | CVSS score                | Rating         ")
                print("---------------------------------------------------------------------------------------")
                print("Eavesdropping                        | 8.0                       | High                ")
                print("Denial of Service                    | 8.5                       | High                ")
                print("Remote Code Execution                | 8.9                       | High                ")
                print("Spoof SIP Status Message Handling    | 6.9                       | Medium              ")
                print("Local File Inclusion                 | 8.0                       | High                ")
            elif search == "ssh" or search == "OpenSSH":
                print("Vul ssh")
            elif search == "http" or search == "nginx":
                print("Vul http")
        else:
            print("There is Vulnerability in database")

        a = input("Do you want to continue to search? Y/Yes or N/No")
        if a == "Y" or a == "y" or a == "yes":
            check=True
        elif a == "N" or a == "n" or a == "no":
            check=False
  
    
    
searchsploit()
    
    
    
    
    
    
    
    