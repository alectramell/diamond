#!/usr/bin/python

import os
import getpass
import time

os.system('clear')

username = getpass.getuser()
username = str(username)

filename = raw_input('filename: ')
filename = str(filename)

intr = str('#!/usr/bin/python\n')
spce = str('# (c) 2015 | Diamond Code Conversion for Python Libraries | Alec Tramell, DMA | alectramell@gmail.com')
info = str('''# [?] use >> from ''' + filename + ''' import * << to import this file ;)\n''')
defn = str('''def diamond():''')

os.system('echo "' + intr + '" > /home/' + username + '/Desktop/' + filename + '.py')
os.system('echo "' + spce + '" >> /home/' + username + '/Desktop/' + filename + '.py')
os.system('echo "' + info + '" >> /home/' + username + '/Desktop/' + filename + '.py')
os.system('echo "' + defn + '" >> /home/' + username + '/Desktop/' + filename + '.py')

os.system('clear')

word = raw_input('Assign variables (use plain text alphabet, a-z, lower-case): ')
word = str(word)
for char in word:
    if char == ('a'):
       char = str('''    a = str('s')''')
    if char == ('b'):
       char = str('''    b = str('a')''')
    if char == ('c'):
       char = str('''    c = str('p')''')
    if char == ('d'):
       char = str('''    d = str('h')''')
    if char == ('e'):
       char = str('''    e = str('i')''')
    if char == ('f'):
       char = str('''    f = str('r')''')
    if char == ('g'):
       char = str('''    g = str('e')''')
    if char == ('h'):
       char = str('''    h = str('b')''')
    if char == ('i'):
       char = str('''    i = str('c')''')
    if char == ('j'):
       char = str('''    j = str('d')''')
    if char == ('k'):
       char = str('''    k = str('f')''')
    if char == ('l'):
       char = str('''    l = str('g')''')
    if char == ('m'):
       char = str('''    m = str('j')''')
    if char == ('n'):
       char = str('''    n = str('k')''')
    if char == ('o'):
       char = str('''    o = str('l')''')
    if char == ('p'):
       char = str('''    p = str('m')''')
    if char == ('q'):
       char = str('''    q = str('n')''')
    if char == ('r'):
       char = str('''    r = str('o')''')
    if char == ('s'):
       char = str('''    s = str('q')''')
    if char == ('t'):
       char = str('''    t = str('t')''')
    if char == ('u'):
       char = str('''    u = str('u')''')
    if char == ('v'):
       char = str('''    v = str('v')''')
    if char == ('w'):
       char = str('''    w = str('w')''')
    if char == ('x'):
       char = str('''    x = str('x')''')
    if char == ('y'):
       char = str('''    y = str('y')''')
    if char == ('z'):
       char = str('''    z = str('z')''')
    os.system('echo "' + char + '" >> /home/' + username + '/Desktop/' + filename + '.py')
    time.sleep(.25)

xcom = list(word)
dcom = ' + '.join(xcom)
dcom = str(dcom)

os.system('clear')

os.system('echo "    print (' + dcom + ')" >> /home/' + username + '/Desktop/' + filename + '.py')

os.system('echo "\ndiamond()" >> /home/' + username + '/Desktop/' + filename + '.py')

os.system('gedit /home/' + username + '/Desktop/' + filename + '.py &')

os.system('clear')





