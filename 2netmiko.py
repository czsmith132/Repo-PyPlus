#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

NXOS1={
  "host": 'nxos1.lasthop.io',
  "username": 'pyclass',  
  "password": getpass(),
  "device_type": 'cisco_nxos_ssh',
  "session_log": 'log_NXOS1.txt'
}
NXOS2={
  "host": 'nxos2.lasthop.io',
  "username": 'pyclass',  
  "password": getpass(),
  "device_type": 'cisco_nxos_ssh',
  "session_log": 'log_NXOS2.txt'
}

devices=[NXOS1,NXOS2]

for device in devices:
  net_connect = ConnectHandler(**device)
  print(net_connect.find_prompt())

#show version
net_connect = ConnectHandler(**NXOS1)
version=net_connect.send_command('show version')
print('\n',version)
