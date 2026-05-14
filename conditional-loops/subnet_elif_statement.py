ip = '192.168.0.1'
subnet = '255.255.255.0'

if subnet.endswith('.0'):
    subnet_slash_notion = '/24'
elif subnet.endswith('.128'):
    subnet_slash_notion = '/25'
elif subnet.endswith('.192'):
    subnet_slash_notion = '/26'
elif subnet.endswith('.224'):
    subnet_slash_notion = '/27'
elif subnet.endswith('.240'):
    subnet_slash_notion = '/28'
elif subnet.endswith('.248'):
    subnet_slash_notion = '/29'
elif subnet.endswith('.252'):
    subnet_slash_notion = '/30'
elif subnet.endswith('.254'):
    subnet_slash_notion = '/31'
elif subnet.endswith('.255'):
    subnet_slash_notion = '/32'
else:
    print('Subnet slash notation could not be determined')

print(ip + subnet_slash_notion)