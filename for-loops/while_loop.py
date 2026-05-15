import netmiko

last_octet =  1
while last_octet <=3:
    ip_address = '10.254.0.' + str(last_octet)
    print(ip_address)
    last_octet += 1