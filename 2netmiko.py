#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

passwd = getpass()

NXOS1={
  "host": 'nxos1.lasthop.io',
  "username": 'pyclass',  
  "password": passwd,
  "device_type": 'cisco_nxos_ssh',
  "session_log": 'log_NXOS1.txt'
}
NXOS2={
  "host": 'nxos2.lasthop.io',
  "username": 'pyclass',  
  "password": passwd,
  "device_type": 'cisco_nxos_ssh',
  "session_log": 'log_NXOS2.txt'
}

devices=[NXOS1,NXOS2]

print('Device Prompts:\n')
for device in devices:
  net_connect = ConnectHandler(**device)
  print(net_connect.find_prompt())


#show version
net_connect = ConnectHandler(**NXOS1)
with open('log-sh_version.txt','w') as f:
  version=net_connect.send_command('show version')
  f.write('\nNXOS1 SH VER\n\n' + version)
