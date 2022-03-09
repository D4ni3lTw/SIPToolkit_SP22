data = {'nmap': {'command_line': 'nmap -oX - -p 20-5100 -sV -O 3.0.94.34 127.0.0.1', 'scaninfo': {'tcp': {'method': 'syn', 'services': '20-5100'}}, 'scanstats': {'timestr': 'Fri Mar  4 00:57:19 2022', 'elapsed': '301.45', 'uphosts': '2', 'downhosts': '0', 'totalhosts': '2'}}, 'scan': {'3.0.94.34': {'hostnames': [{'name': 'ec2-3-0-94-34.ap-southeast-1.compute.amazonaws.com', 'type': 'PTR'}], 'addresses': {'ipv4': '3.0.94.34'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'reset'}, 'uptime': {'seconds': '194596', 'lastboot': 'Tue Mar  1 18:51:11 2022'}, 'tcp': {22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 
'OpenSSH', 'version': '7.4', 'extrainfo': 'protocol 2.0', 'conf': '10', 'cpe': 'cpe:/a:openbsd:openssh:7.4'}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.20.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:igor_sysoev:nginx:1.20.1'}, 443: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'nginx', 'version': '1.20.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:igor_sysoev:nginx:1.20.1'}, 5060: {'state': 'open', 'reason': 'syn-ack', 'name': 'sip', 'product': 'FreeSWITCH', 'version': '', 'extrainfo': 'Status: 200 OK', 'conf': '10', 'cpe': ''}, 5080: {'state': 'open', 'reason': 'syn-ack', 'name': 'sip', 'product': 'FreeSWITCH', 'version': '', 'extrainfo': 'Status: 200 OK', 'conf': '10', 'cpe': ''}}, 'portused': [{'state': 'open', 'proto': 'tcp', 'portid': '22'}], 'osmatch': [{'name': 'Linux 2.6.32', 'accuracy': '93', 'line': '55366', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:2.6.32']}]}, {'name': 'Linux 3.10 - 4.11', 'accuracy': '93', 'line': '63442', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}]}, {'name': 'Linux 3.2 - 4.9', 'accuracy': '93', 'line': '65317', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}]}, {'name': 'Linux 3.4 - 3.10', 'accuracy': '93', 'line': '65578', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 4.15 - 5.6', 'accuracy': '93', 'line': '67241', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '4.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:4']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '93', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 2.6.32 - 3.10', 'accuracy': '92', 'line': '56574', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:2.6']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 2.6.32 - 3.13', 'accuracy': '92', 'line': '56604', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:2.6']}, {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '3.X', 'accuracy': '92', 'cpe': ['cpe:/o:linux:linux_kernel:3']}]}, {'name': 'Linux 5.0 - 5.3', 'accuracy': '91', 'line': '68085', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 5.0 - 5.4', 'accuracy': '91', 'line': '68106', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5']}]}, {'name': 'Linux 5.4', 'accuracy': '91', 'line': '68179', 'osclass': [{'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '5.X', 'accuracy': '91', 'cpe': ['cpe:/o:linux:linux_kernel:5.4']}]}]}, '127.0.0.1': {'hostnames': [{'name': 'removeallblocksite.SW', 'type': 'PTR'}], 'addresses': {'ipv4': '127.0.0.1'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'localhost-response'}, 'tcp': {135: {'state': 'open', 'reason': 'syn-ack', 'name': 'msrpc', 'product': 'Microsoft Windows RPC', 'version': '', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/o:microsoft:windows'}, 137: {'state': 'filtered', 'reason': 'no-response', 'name': 'netbios-ns', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'microsoft-ds', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 903: {'state': 'open', 'reason': 'syn-ack', 'name': 'vmware-auth', 'product': 'VMware Authentication Daemon', 'version': '1.10', 'extrainfo': 'Uses VNC, SOAP', 'conf': '10', 'cpe': ''}, 913: {'state': 'open', 'reason': 'syn-ack', 'name': 'vmware-auth', 'product': 'VMware Authentication Daemon', 'version': '1.0', 'extrainfo': 'Uses VNC, SOAP', 'conf': '10', 'cpe': ''}, 1001: {'state': 'filtered', 'reason': 'no-response', 'name': 'webpush', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1042: {'state': 'open', 'reason': 'syn-ack', 'name': 'afrog', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1043: {'state': 'open', 'reason': 'syn-ack', 'name': 'boinc', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1220: {'state': 'filtered', 'reason': 'no-response', 'name': 'quicktime', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1439: {'state': 'filtered', 'reason': 'no-response', 'name': 'eicon-x25', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 1877: {'state': 'filtered', 'reason': 'no-response', 'name': 'hp-webqosdb', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 2096: {'state': 'filtered', 'reason': 'no-response', 'name': 'nbx-dir', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 2315: {'state': 'filtered', 'reason': 'no-response', 'name': 'precise-sft', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3213: {'state': 'open', 'reason': 'syn-ack', 'name': 'neon24x7', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5040: {'state': 'open', 'reason': 'syn-ack', 'name': 'unknown', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}, 'portused': [{'state': 'open', 'proto': 'tcp', 'portid': '135'}, {'state': 'closed', 'proto': 'tcp', 'portid': '20'}, {'state': 'closed', 'proto': 'udp', 'portid': '40578'}], 'osmatch': [{'name': 'Microsoft Windows 10 1809 - 1909', 'accuracy': '100', 'line': '69956', 'osclass': [{'type': 'general purpose', 'vendor': 'Microsoft', 'osfamily': 'Windows', 'osgen': '10', 'accuracy': '100', 'cpe': ['cpe:/o:microsoft:windows_10']}]}]}}}

json_data = data['scan'].items()

for key, value in json_data:
    for port in json_data['tcp']:print(port[0])













































