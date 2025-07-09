#!/usr/bin/env python

from netmiko import ConnectHandler
#from getpass import getpass

#passwd = getpass()
from devices_import import * 

#NXOS1={
#  "host": 'nxos1.lasthop.io',
#  "username": 'pyclass',  
#  "password": passwd,
#  "device_type": 'cisco_nxos_ssh',
#  "session_log": 'log_NXOS1.txt'
#}
#NXOS2={...}
#cisco4={...}

devices=[cisco4]

#print('Device Prompts:\n')
#for device in devices:
#  net_connect = ConnectHandler(**device)
#  print(net_connect.find_prompt())


#extended ping
net_connect = ConnectHandler(**cisco4)
net_connect.send_command('ping',expect_string=r':')
net_connect.send_command('\n',expect_string=r':')
net_connect.send_command('8.8.8.8',expect_string=r':')
net_connect.send_command('\n',expect_string=r':')
net_connect.send_command('\n',expect_string=r':')
net_connect.send_command('\n',expect_string=r':')
net_connect.send_command('\n',expect_string=r':')
#execution=net_connect.send_command('\n',expect_string=r':')
print(net_connect.send_command('\n',expect_string=r':'))

#print(execution)
