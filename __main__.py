#!/usr/bin/python

import os
import getpass

os.system('clear')

dlink = raw_input('Translate Diamond Code: ')
dlink = str(dlink)
dlink = dlink.decode('hex')
dlink = str(dlink)

os.system('clear')

getlink = str('touch ~/Desktop/diamond-code.txt')

echocode = str('echo "' + dlink + '" > ~/Desktop/diamond-code.txt')

os.system(echocode)
os.system(getlink)
os.system('gedit ~/Desktop/diamond-code.txt')

os.system('clear')
