ip = '192.168.0.1'
subnet = '255.255.255.0'

if subnet.endswith('.0'):
    subnet_slash_notion = '/24'
    print(ip + subnet_slash_notion)

else:
    print('Subnet slash notation could not be determined')