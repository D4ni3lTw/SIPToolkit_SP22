from cvss import CVSS2, CVSS3
# This is array after scanning target and append info
db=['ssh', 'OpenSSH', '7.4', 'http', 'nginx', '1.20.1', 'sip', 'FreeSWITCH']

def searchsploit():
    check = True
    while check == True:
        search=input("Search vulnerability:")
        if search in db:
            if search == "sip" or search == "SIP" or search == "FreeSWITCH":
                print("------------------------------------------")
                print("Vulnerabe VOIP Title                      ")
                print("------------------------------------------")
                print("Eavesdropping                             ")
                print("Denial of Service                         ")
                print("Event Socket Command Execution            ")
                print("Spoof SIP Status Message Handling         ")
                print("Local File Inclusion                      ")
            elif search == "ssh" or search == "OpenSSH":
                print("Vul ssh")
            elif search == "http" or search == "nginx":
                print("Vul http")
        else:
            print("There is Vulnerability in database")

        a = input("Do you want to continue to search? Y/Yes or N/No: ")
        if a == "Y" or a == "y" or a == "yes":
            check=True
        elif a == "N" or a == "n" or a == "no":
            check=False

searchsploit()

# Function Calculate score  based on CVSS ver 3.0
def Calculate_CVSS():
    check=True
    while check == True: #Create a loop
        vul = input("Enter vulnerability to calculate: ")
        if vul == "Eavesdropping" or vul == "eavesdropping":
            metric = input("Enter vector: ") #Input metric
            c = CVSS3(metric)
            c = c.scores() # Type of score format is (float, float, float)
            cvs = dict()
            cvslist = list()
            print("Eavesdropping score: ",c)
            for score in c:
                score = float(score)
                # Create a if/elif/else to find qualitative rating
                if score <=0.0:
                    cvslist.append("None")
                elif score >=0.1 and score <=3.9:
                    cvslist.append("Low")
                elif score >=4.0 and score <=6.9:
                    cvslist.append("Medium")
                elif score >=7.0 and score <=8.9:
                    cvslist.append("High")
                elif score >=9.0 and score <=10.0:
                    cvslist.append("Critical")
                else:
                    print("Nothing")
            cvs['base_metric']=cvslist[0] 
            cvs['temporal_metric']=cvslist[1]
            cvs['environment_metric']=cvslist[2]
            # Print Qualitative after getting score
            print("-----------------------")
            print("Qualitative Rating     ")
            print("-----------------------")
            print("Base_metric:",cvs["base_metric"])
            print("Temp_metric:",cvs["temporal_metric"])
            print("Environmental_metric:",cvs["environment_metric"])

        elif vul == "DoS" or vul == "Denial of Service":
            metric = input("Enter vector: ")
            c = CVSS3(metric)
            c = c.scores()
            cvs = dict()
            cvslist = list()
            print("DoS score: ",c)
            for score in c:
                score = float(score)
                if score <=0.0:
                    cvslist.append("None")
                elif score >=0.1 and score <=3.9:
                    cvslist.append("Low")
                elif score >=4.0 and score <=6.9:
                    cvslist.append("Medium")
                elif score >=7.0 and score <=8.9:
                    cvslist.append("High")
                elif score >=9.0 and score <=10.0:
                    cvslist.append("Critical")
                else:
                    print("Nothing")
            cvs['base_metric']=cvslist[0]
            cvs['temporal_metric']=cvslist[1]
            cvs['environment_metric']=cvslist[2]
            print("-----------------------")
            print("Qualitative Rating     ")
            print("-----------------------")
            print("Base_metric:",cvs["base_metric"])
            print("Temp_metric:",cvs["temporal_metric"])
            print("Environmental_metric:",cvs["environment_metric"])
        
        elif vul == "Spoof SIP" or vul == "spoof sip":
            metric = input("Enter vector: ")
            c = CVSS3(metric)
            c = c.scores()
            cvs = dict()
            cvslist = list()
            print("Spoof SIP score: ",c)
            for score in c:
                score = float(score)
                if score <=0.0:
                    cvslist.append("None")
                elif score >=0.1 and score <=3.9:
                    cvslist.append("Low")
                elif score >=4.0 and score <=6.9:
                    cvslist.append("Medium")
                elif score >=7.0 and score <=8.9:
                    cvslist.append("High")
                elif score >=9.0 and score <=10.0:
                    cvslist.append("Critical")
                else:
                    print("Nothing")
            cvs['base_metric']=cvslist[0]
            cvs['temporal_metric']=cvslist[1]
            cvs['environment_metric']=cvslist[2]
            print("-----------------------")
            print("Qualitative Rating     ")
            print("-----------------------")
            print("Base_metric:",cvs["base_metric"])
            print("Temp_metric:",cvs["temporal_metric"])
            print("Environmental_metric:",cvs["environment_metric"])
        
        elif vul == "command execution":
            metric = input("Enter vector: ")
            c = CVSS3(metric)
            c = c.scores()
            cvs = dict()
            cvslist = list()
            print("CE score: ",c)
            for score in c:
                score = float(score)
                if score <=0.0:
                    cvslist.append("None")
                elif score >=0.1 and score <=3.9:
                    cvslist.append("Low")
                elif score >=4.0 and score <=6.9:
                    cvslist.append("Medium")
                elif score >=7.0 and score <=8.9:
                    cvslist.append("High")
                elif score >=9.0 and score <=10.0:
                    cvslist.append("Critical")
                else:
                    print("Nothing")
            cvs['base_metric']=cvslist[0]
            cvs['temporal_metric']=cvslist[1]
            cvs['environment_metric']=cvslist[2]
            print("-----------------------")
            print("Qualitative Rating     ")
            print("-----------------------")
            print("Base_metric:",cvs["base_metric"])
            print("Temp_metric:",cvs["temporal_metric"])
            print("Environmental_metric:",cvs["environment_metric"])

        elif vul == "local file inclusion":
            metric = input("Enter vector: ")
            c = CVSS3(metric)
            c = c.scores()
            cvs = dict()
            cvslist = list()
            print("LFI score: ",c)
            for score in c:
                score = float(score)
                if score <=0.0:
                    cvslist.append("None")
                elif score >=0.1 and score <=3.9:
                    cvslist.append("Low")
                elif score >=4.0 and score <=6.9:
                    cvslist.append("Medium")
                elif score >=7.0 and score <=8.9:
                    cvslist.append("High")
                elif score >=9.0 and score <=10.0:
                    cvslist.append("Critical")
                else:
                    print("Nothing")
            cvs['base_metric']=cvslist[0]
            cvs['temporal_metric']=cvslist[1]
            cvs['environment_metric']=cvslist[2]
            print("-----------------------")
            print("Qualitative Rating     ")
            print("-----------------------")
            print("Base_metric:",cvs["base_metric"])
            print("Temp_metric:",cvs["temporal_metric"])
            print("Environmental_metric:",cvs["environment_metric"])


        else:
            print("There is no vulner in DB")

        a = input("Do you want to continue to calculate? Y/Yes or N/No: ")
        if a == "Y" or a == "y" or a == "yes":
            check=True
        elif a == "N" or a == "n" or a == "no":
            check=False

Calculate_CVSS()
