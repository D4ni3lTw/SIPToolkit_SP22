def ensure_enviroment():
    try:
        import sys
        import math
        import nmap
        # import wireshark
        print('OK')
    except ModuleNotFoundError or ImportError as ee:
        print('This script can only be run in blabla environment : {0}'.format(ee.msg), file=sys.stderr)
        exit(1)

