def ip_spliter(ips):
    if ' ' in ips:
        ip = ips.split(' ')
        return ip
        # print(ip)
    else:
        return [ips]

def data_parse(ips, data):
    print('---------------------------------------------------------------')
    print('Scanning Result!')
    print('---------------------------------------------------------------')
    ip = ip_spliter(ips)
    scan_data = data['scan']
    for singleip in ip:
        if scan_data is not None:
            hostname = scan_data[str(singleip)]['hostnames'][0]['name']
            if 'mac' in scan_data[str(singleip)]['addresses']:
                macaddr = scan_data[str(singleip)]['addresses']['mac']
            else:
                macaddr = ''
            if 'vendor' in scan_data[str(singleip)]:
                vendor = scan_data[str(singleip)]['vendor']

            host_state = scan_data[str(singleip)]['status']['state']
            host_state_reason = scan_data[str(singleip)]['status']['reason']
            if 'tcp' in scan_data[str(singleip)]:
                tcp = scan_data[str(singleip)]['tcp']
                portlist = list(tcp.keys())
                for port in portlist:
                    port_num = port
                    port_state = tcp[port]['state']
                    port_state_reason = tcp[port]['reason']
                    port_name = tcp[port]['name']
                    port_product = tcp[port]['product']
                    port_product_version = tcp[port]['version']
                    port_cpe = tcp[port]['cpe']
                    if 'script' in tcp:
                        port_script = tcp[port]['script']

            if 'udp' in scan_data[str(singleip)]:
                udp = scan_data[str(singleip)]['udp']
                u_portlist = list(udp.keys())
                for u_port in u_portlist:
                    u_port_num = u_port
                    u_port_state = udp[port]['state']
                    u_port_state_reason = udp[port]['reason']
                    u_port_name = udp[port]['name']
                    u_port_product = udp[port]['product']
                    u_port_product_version = udp[port]['version']
                    u_port_cpe = udp[port]['cpe']
                    if 'script' in udp:
                        u_port_script = udp[port]['script']

            if 'osmatch' in scan_data[str(singleip)]:
                osmatch = scan_data[str(singleip)]['osmatch'][0]
                osname = osmatch['name']
                osaccuracy = osmatch['accuracy']
                oscpe = osmatch['osclass'][0]['cpe'][0]

        print("\033[1mScan report for IP {0}\033[0m".format(singleip))
        if hostname != '':
            print('IPV4: ', singleip ,' - ', hostname)
        else:
            print('IPV4: ', singleip)

        #MAC Address
        if macaddr != '':
            print(' -Mac address: ',macaddr)

        #Host state
        if host_state.casefold() == 'up':
            print('Host status: \033[92m{0}\033[0m'.format(host_state))
        else:
            print('Host status: \033[91m{0}\033[0m'.format(host_state))

        if host_state.casefold() == 'up':

            print("   PORT    STATE         SERVICE")
            for port in portlist:
                port_num = port
                port_state = tcp[port]['state']
                port_state_reason = tcp[port]['reason']
                port_name = tcp[port]['name']
                port_product = tcp[port]['product']
                port_product_version = tcp[port]['version']
                port_cpe = tcp[port]['cpe']

                if port_state.casefold() == 'open':
                    print("{0:>5s}/{1:3s}  \033[92m{2:12s}\033[0m {3} {4}({5})".format(
                        str(port), 'tcp', port_state, port_product, port_product_version, port_name
                    ))
                    if 'script' in tcp:
                        port_script = tcp[port]['script']
                        print('')
                else:
                    print("{0:>5s}/{1:3s}  \033[93m{2:12s}\033[0m {3} {4}({5})".format(
                        str(port), 'tcp', port_state, port_product, port_product_version, port_name
                    ))
                    if 'script' in tcp:
                        port_script = tcp[port]['script']
                        print('')

                print("\nOS Fingerprint:")
                print(' -OS Name: ', osname)
                print(' -Accuracy: ',osaccuracy)
                print(' -CPE: ', oscpe)
            print('')

#From port scanning CPE into vendor-product
def cpe_spliter(ips, data):
    ip = ip_spliter(ips)
    scan_data = data['scan']
    for singleip in ip:
        if scan_data is not None:
            if 'tcp' in scan_data[str(singleip)]:
                tcp = scan_data[str(singleip)]['tcp']
                portlist = list(tcp.keys())
                for port in portlist:
                    port_num = port
                    port_cpe = tcp[port]['cpe']


<<<<<<< HEAD
=======
# data = {'nmap': {'command_line': 'nmap -oX - -p 20-5100 -sV -O 3.0.94.34 127.0.0.1', 'scaninfo': {'tcp': {'method': 'syn', 'services': '20-5100'}}, 'scanstats': {'timestr': 'Fri Mar  4 00:57:19 2022', 'elapsed': '301.45', 'uphosts': '2', 'downhosts': '0', 'totalhosts': '2'}}, 'scan': {'3.0.94.34': {'hostnames': [{'name': 'ec2-3-0-94-34.ap-southeast-1.compute.amazonaws.com', 'type': 'PTR'}], 'addresses': {'ipv4': '3.0.94.34'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'reset'}, 'uptime': {'seconds': '194596', 'lastboot': 'Tue Mar  1 18:51:11 2022'}, 'tcp': {22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 
# 'OpenSSH', 'version': '7.4', 'extrainfo': 'protocol 2.0', 'conf': '10', 'cpe': 'cpe:/a:openbsd:openssh:7.4'}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.20.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:igor_sysoev:nginx:1.20.1'}, 443: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.20.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:igor_sysoev:nginx:1.20.1'}, 5060: {'state': 'open', 'reason': 'syn-ack', 'name': 'sip', 'product': 'FreeSWITCH', 'version': '', 'extrainfo': 'Status: 200 OK', 'conf': '10', 'cpe': ''}, 5080: {'state': 'open', 'reason': 'syn-ack', 'name': 'sip', 'product': 'FreeSWITCH', 'version': '', 'extrainfo': 'Status: 200 OK', 'conf': '10', 'cpe': ''}}, 'portused': [{'state': 'open', 'proto': 'tcp', 'portid': '22'}], 'osmatch': [{'name': 'Linux 2.6.32', 'accuracy': '93', 'line': '55366', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:2.6.32']}]}, {'name': 'Linux 3.10 - 4.11', 'accuracy': '93', 'line': '63442', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}]}, {'name': 'Linux 3.2 - 4.9', 'accuracy': '93', 'line': '65317', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}]}, {'name': 'Linux 3.4 - 3.10', 'accuracy': '93', 'line': '65578', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 4.15 - 5.6', 'accuracy': '93', 'line': '67241', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 2.6.32 - 3.10', 'accuracy': '92', 'line': '56574', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:2.6']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 2.6.32 - 3.13', 'accuracy': '92', 'line': '56604', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:2.6']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 5.0 - 5.3', 'accuracy': '91', 'line': '68085', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 5.0 - 5.4', 'accuracy': '91', 'line': '68106', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 5.4', 'accuracy': '91', 'line': '68179', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5.4']}]}]}, '127.0.0.1': {'hostnames': [{'name': 'removeallblocksite.SW', 'type': 'PTR'}], 'addresses': {'ipv4': '127.0.0.1'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'localhost-response'}, 'tcp': {135: {'state': 'open', 'reason': 'syn-ack', 'name': 'msrpc', 'product': 'Microsoft Windows RPC', 'version': '', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/o:microsoft:windows'}, 137: {'state': 'filtered', 'reason': 'no-response', 'name': 'netbios-ns', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'microsoft-ds', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 903: {'state': 'open', 'reason': 'syn-ack', 'name': 'vmware-auth', 'product': 'VMware Authentication Daemon', 'version': '1.10', 'extrainfo': 'Uses VNC, SOAP', 'conf': '10', 'cpe': ''}, 913: {'state': 'open', 'reason': 'syn-ack', 'name': 'vmware-auth', 'product': 'VMware Authentication Daemon', 'version': '1.0', 'extrainfo': 'Uses VNC, SOAP', 'conf': '10', 'cpe': ''}, 1001: {'state': 'filtered', 'reason': 'no-response', 'name': 'webpush', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1042: {'state': 'open', 'reason': 'syn-ack', 'name': 'afrog', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1043: {'state': 'open', 'reason': 'syn-ack', 'name': 'boinc', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1220: {'state': 'filtered', 'reason': 'no-response', 'name': 'quicktime', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1439: {'state': 'filtered', 'reason': 'no-response', 'name': 'eicon-x25', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1877: {'state': 'filtered', 'reason': 'no-response', 'name': 'hp-webqosdb', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 2096: {'state': 'filtered', 'reason': 'no-response', 'name': 'nbx-dir', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 2315: {'state': 'filtered', 'reason': 'no-response', 'name': 'precise-sft', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3213: {'state': 'open', 'reason': 'syn-ack', 'name': 'neon24x7', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5040: {'state': 'open', 'reason': 'syn-ack', 'name': 'unknown', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}, 'portused': [{'state': 'open', 'proto': 'tcp', 'portid': '135'}, {'state': 'closed', 'proto': 'tcp', 'portid': '20'}, {'state': 'closed', 'proto': 'udp', 'portid': '40578'}], 'osmatch': [{'name': 'Microsoft Windows 10 1809 - 1909', 'accuracy': '100', 'line': '69956', 'osclass': [{'type': 'general purpose', 'vendor': 'Microsoft', 'osfamily': 'Windows', 'osgen': '10', 'accuracy': '100', 'cpe': ['cpe:/o:microsoft:windows_10']}]}]}}}

# ips = '3.0.94.34 127.0.0.1'

# data_parse(ips, data)

>>>>>>> ed714477eb1e43c83f0580b117a209a16dfc03a7



