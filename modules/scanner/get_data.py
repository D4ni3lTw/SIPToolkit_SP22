from libnmap.parser import NmapParser, NmapParserException

def icmp_sweep(nmap_report, ip):
    print(nmap_report.get_host_byid(ip))

def port_scanning(nmap_report):
    print(
        "Starting Nmap {0} ( http://nmap.org ) at {1}".format(
            nmap_report.version, nmap_report.started
        )
    )

    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(tmp_host, host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                str(serv.port), serv.protocol, serv.state, serv.service
            )
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)

def os_fingerprint(rep):
    print("{0}/{1} hosts up".format(rep.hosts_up, rep.hosts_total))
    for _host in rep.hosts:
        if _host.is_up():
            print("{0} {1}".format(_host.address, " ".join(_host.hostnames)))
            if _host.os_fingerprinted:
                print("OS Fingerprint:")
                msg = ""
                for osm in _host.os.osmatches:
                    print("Found Match:{0} ({1}%)".format(osm.name, osm.accuracy))
                    for osc in osm.osclasses:
                        print("\tOS Class: {0}".format(osc.description))
                        for cpe in osc.cpelist:
                            print("\tCPE: {0}".format(cpe.cpestring))
            else:
                print("No fingerprint available")