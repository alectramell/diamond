#!/usr/bin/python

import os
import getpass

os.system('clear')

dlink = raw_input('Redeem Diamond Code: ')
dlink = str(dlink)
dlink = dlink.decode('hex')
dlink = str(dlink)

os.system('clear')

getlink = str('cd ~/Desktop && wget ' + dlink + ' && clear && echo "DOWNLOAD FINISHED! Check ~/Desktop/.."')

os.system(getlink)
