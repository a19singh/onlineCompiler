#!/usr/bin/python36
print("content-type:text/html")
print()

print("<html>")
print("<head>")
print("Compiler")
print("</head>")
print("<body><form action=\"/cgi-bin/dustbin/compiler.py\">")
print("<textarea rows=\"30\" cols=\"90\" name=\"code\">")
print("#Type Your Text Here!!")
print("</textarea></br>")
print("<input type=\"submit\" value=\"Submit\"/>")
print("</form></body></html>")

