from bin.exploit import exploit
from bin.misc import loadscreen
from bin.report import report
from bin.scanning import scanning
from bin.vulnassesst import vulnassesst
from py_console import console

def main():
    #Starting Process
    try:
        loadscreen()
    except Exception as e:
        console.error("An Error Occurred!!!")
        console.error(e)
    except:
        console.error("Faill to start the program!!",
                    "\nPlease read the document for fearther information!!")

    #Main program function
    try:
        ipaddr = input("Enter your choice: ")
        scanning(ipaddr)
        vulnassesst()
        exploit()
        report()
        print()
        console.success("Running cycle complete successfully!")
    except Exception as e:
        console.error("An Error Occurred!!!")
        console.error(e)
    except:
        console.error("Unexpected Error Occurred!!!")


if __name__ == '__main__':
    main()
