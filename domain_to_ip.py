#Domain_to_ip_convator 

import socket

#import pyfiglet

# Display banner using pyfiglet
#banner = pyfiglet.figlet_format("Domain to IP Converter")
#print(banner)

# Input domain name
domain_name = input("Enter your target domain: ")

try:
    # Get IP address from domain name
    ip = socket.gethostbyname(domain_name)
    print(f"The IP address of {domain_name} is: {ip}")
except socket.gaierror:
    print("Invalid domain name or unable to resolve the domain.")
