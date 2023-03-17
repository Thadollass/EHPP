#!/bin/python


        import socket 

with open('target.txt', 'r') as f_in, open('ip_addresses.txt', 'w') as f_out:
    for target_host in f_in:
        target_host = target_host.strip()
        target_ip = socket.gethostbyname(target_host)
        f_out.write(f"IP address for {target_host} is {target_ip}\n")