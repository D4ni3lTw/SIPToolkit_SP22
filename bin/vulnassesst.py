from modules.vulnassess import cve_search
from py_console import console
import sys

def vulnassesst(vendor,product):
    if ( vendor is not None and product is not None ):
        try:
            api = cve_search.get_api(vendor, product)
            cve_search.get_data(api)
            return api
        except Exception as e:
            console.error("An Error Occurred!")
            console.error(e)
            sys.exit(1)
        except:
            console.error("Unexpected Error Occurred")
            sys.exit(1)