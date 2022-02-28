# Vulnerable Assessment

import nmap

nm=nmap.PortScanner()
def scan_port():
   ip=input("Enter ip target:")
   ip_addr=str(ip)
   result=nm.scan(ip_addr,'20-5100','-sV')
   return result

# Append data from json to array
def AppendDataToArray():
   data=scan_port()
   if data is None:
      print("No data")
   else:
      info_arr=[]
      service_ssh=data['scan']['192.168.50.145']['tcp'][22]['name']
      product_ssh=data['scan']['192.168.50.145']['tcp'][22]['product']
      version_ssh=data['scan']['192.168.50.145']['tcp'][22]['version']

      service_http=data['scan']['192.168.50.145']['tcp'][80]['name']
      product_http=data['scan']['192.168.50.145']['tcp'][80]['product']
      version_http=data['scan']['192.168.50.145']['tcp'][80]['version']

      service_sip=data['scan']['192.168.50.145']['tcp'][5060]['name']
      product_sip=data['scan']['192.168.50.145']['tcp'][5060]['product']

      info_arr.append(service_ssh)
      info_arr.append(product_ssh)
      info_arr.append(version_ssh)
      info_arr.append(service_http)
      info_arr.append(product_http)
      info_arr.append(version_http)
      info_arr.append(service_sip)
      info_arr.append(product_sip)

      return info_arr

def searchvulner():
   arr=AppendDataToArray()
   print(arr)
   check = True
   while check == True:
      search=input("Search vulnerability:")
      if search in arr:
         if search == "sip"  or search == "FreeSWITCH":
            print("------------------------------------------------------------------------------------")
            print("Vulnerabe VOIP Title                 | CVSS score                | Rating           ")
            print("------------------------------------------------------------------------------------")
            print("Eavesdropping                        | 8.0                       | High             ")
            print("Denial of Service                    | 8.5                       | High             ")
            print("Remote Code Execution                | 8.9                       | High             ")
            print("Spoof SIP Status Message Handling    | 6.9                       | Medium           ")
            print("Local File Inclusion                 | 8.0                       | High             ")
         elif search == "ssh" or search == "OpenSSH":
            print("------------------------------------------------------------------------------------")
            print("Vulnerabe SSH Title                           | CVSS score                | Rating  ")
            print("------------------------------------------------------------------------------------")
            print("OpenSSH < 7.7 - Username enumeration          | 8.0                       | High    ")
            print("Denial of Service                             | 8.5                       | High    ")
            print("Remote Code Execution                         | 8.9                       | High    ")
            print("Remote SELinux Privilege Escalation           | 6.9                       | Medium  ")
            print("Duplicated Block Remote Denial of Service     | 8.0                       | High    ")
         elif search == "http" or search == "nginx":
            print("------------------------------------------------------------------------------------")
            print("Vulnerabe HTTP Title                 | CVSS score                | Rating           ")
            print("------------------------------------------------------------------------------------")
            print("Directory Traversal                  | 8.0                       | High             ")
            print("Denial of Service                    | 8.5                       | High             ")
            print("Remote Code Execution                | 8.9                       | High             ")
            print("Brute Force                          | 6.9                       | Medium           ")
            print("Local File Inclusion                 | 8.0                       | High             ")
   else:
      print("There is no Vulnerability in database ")

   a = input("Do you want to continue to search? Y/Yes or N/No: ")
   if a == "Y" or a == "y" or a == "yes":
      check=True
   elif a == "N" or a == "n" or a == "no":
      check=False

searchvulner()