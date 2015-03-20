#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

mkshell = str('BINPASS=$(zenity --password --title="Authenticate for Install..") && echo $BINPASS | sudo -S chmod 755 ~/diamond/diamond && echo $BINPASS | sudo -S cp ~/diamond/diamond /usr/local/bin/diamond')

os.system(mkshell)
