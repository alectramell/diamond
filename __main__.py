#!/usr/bin/python

import os
import getpass

os.system('clear')

dlink = raw_input('Redeem Diamond Code: ')
dlink = str(dlink)
dlink = dlink.decode('hex')
dlink = str(dlink)

os.system('clear')

getlink = str('cd ~/Desktop && git clone http://github.com/ ' + dlink + '.git && clear && echo "DOWNLOAD FINISHED! Check ~/Desktop/.."')

os.system(getlink)
