def ensure_enviroment():
    try:
        import sys
        import nmap
        import py_console
        import pyfiglet
        import PyInquirer
    except ModuleNotFoundError or ImportError:
        print("\033[1mYour system is missing required modules to run this program!!\nTry using these command to resolve the problem!!!\033[0m",
                "\n\033[93mpip install nmap \npip install py_console \npip install pyfiglet \npip install PyInquirer\033[0m")
        sys.exit(1)