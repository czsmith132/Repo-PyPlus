#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

NXOS1 ={
  "host": 'nxos1.lasthop.io',
  "username": 'pyclass',  
  "password": getpass(),
  "device_type": 'cisco_nxos_ssh',
  "session_log": 'log_NXOS1.txt'
}

net_connect = ConnectHandler(**NXOS1)
print(net_connect.find_prompt())

