#!/usr/bin/python36

print('content-type: text/html')
print()

import cgi
data = cgi.FieldStorage()
cmd = data.getvalue('code')

import subprocess as sp

sp.getoutput('sudo echo "{0}" > code.py'.format(cmd))

print('output: <br>\n')

x = sp.getoutput('sudo python36 code.py')

print(x)

