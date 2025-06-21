#Lab Devices for Pynet Lab
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
