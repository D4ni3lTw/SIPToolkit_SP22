def ip_spliter(ips):
    if ' ' in ips:
        ip = ips.split(' ')
        return ip
        # print(ip)
    else:
        return [ips]

def data_parse(ips, data):
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

        print('---------------------------------------------------------------')
        print('Scanning Result!')
        print('---------------------------------------------------------------')
        print('Hostname:')
        if hostname != '':
            print(' -IPV4: ', singleip ,' - ', hostname)
        else:
            print(' -IPV4: ', singleip)
        print(' -Host status: ', host_state)
        if macaddr != '':
            print(' -Mac address: ',macaddr)
        if host_state == 'up':
            print('OS Match:')
            print(' -OS Name: ', osname)
            print(' -Accuracy: ',osaccuracy)
            print(' -CPE: ', oscpe)

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






