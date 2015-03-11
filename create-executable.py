#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

mkcode = str('''
[Desktop Entry]
Name=Diamond
Comment=Diamond Python Encode Utility
Categories=GNOME;Utility;
Exec=python /home/''' + username + '''/diamond/__main__.py
Icon=/home/''' + username + '''/diamond/icons/diamond64x64.png
Terminal=true
Type=Application
''')

mkdesk = str('echo "' + mkcode + '" > /home/' + username + '/diamond/diamond.desktop && chmod +x /home/' + username + '/diamond/*.desktop && mv /home/' + username + '/diamond/diamond.desktop /home/' + username + '/Desktop/diamond.desktop')

os.system(mkdesk)

os.system('clear')

os.system('NEWSHORT=$(zenity --info --title="Diamond for Ubuntu" --text="~/Desktop/Diamond created!") && clear')

