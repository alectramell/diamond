#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

dlink = str('''
[Desktop Entry]
Name=Create Executable
Comment=Diamond Python Encode Utility
Categories=GNOME;Utility;
Exec=python /home/''' + username + '''/diamond/create-executable.py
Icon=/home/''' + username + '''/diamond/icons/ubuntu64x64.png
Terminal=false
Type=Application
''')

mkshortcut = str('echo "' + dlink + '" > /home/' + username + '/diamond/create-executable.desktop')
actshort = str('chmod +x /home/' + username + '/diamond/create-executable.desktop')
os.system(mkshortcut)
os.system(actshort)

os.system('clear')

word = raw_input("Translate DIAMOND to TEXT: ")
word = list(word)

output = ' + '.join(word)
output = str(output)

text = str('print (' + output + ')')

document = str('''
tlib = str('abcdefghijklmnopqrstuvwxyz')
tlib = list(tlib)
dlib = str('saphirebcdfgjklmnoqtuvwxyz')
dlib = list(dlib)
space = (' ')

N = str(space)
s = str(tlib[0])
a = str(tlib[1])
p = str(tlib[2])
h = str(tlib[3])
i = str(tlib[4])
r = str(tlib[5])
e = str(tlib[6])
b = str(tlib[7])
c = str(tlib[8])
d = str(tlib[9])
f = str(tlib[10])
g = str(tlib[11])
j = str(tlib[12])
k = str(tlib[13])
l = str(tlib[14])
m = str(tlib[15])
n = str(tlib[16])
o = str(tlib[17])
q = str(tlib[18])
t = str(tlib[19]) 
u = str(tlib[20])
v = str(tlib[21])
w = str(tlib[22])
x = str(tlib[23])
y = str(tlib[24])
z = str(tlib[25])

''' + text + '''

''')

com1 = str('echo "#!/usr/bin/python" > ~/Desktop/code.py')
com2 = str('echo "' + document + '" >> ~/Desktop/code.py')

os.system(com1)
os.system(com2)

os.system('python ~/Desktop/code.py > ~/Desktop/.dmsg && rm -r ~/Desktop/code.py && clear')

os.system('touch ~/Desktop/.diamond-msg.sh')

os.system('echo "#!/bin/bash\n" > ~/Desktop/.diamond-msg.sh')
os.system('echo "clear\n" >> ~/Desktop/.diamond-msg.sh')
os.system('echo "cat ~/Desktop/.dmsg && read && clear\n" >> ~/Desktop/.diamond-msg.sh')

os.system('chmod +x ~/Desktop/.diamond-msg.sh')

os.system('gnome-terminal --title="..Diamond | Translation | press [ENTER] to exit.." -x sh -c "~/Desktop/./.diamond-msg.sh && rm -r ~/Desktop/.dmsg && rm -r ~/Desktop/.diamond-msg.sh"')

os.system('clear')









