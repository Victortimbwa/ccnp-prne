# For loops are used to iterate over strings, lists, tuples, sets, dictonaries, and other iterable objects.
import netmiko

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'

net_connect = netmiko.ConnectHandler(ip=ip, username=username, password=password, device_type=device_type)
sh_ip_int = net_connect.send_command('show ip int brief')
print(sh_ip_int)