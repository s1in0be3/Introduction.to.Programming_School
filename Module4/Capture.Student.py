import cgi

data = cgi.FieldStorage() #there is a errormessage here: "cannot find refrence 'frieldstorage' in 'cgi.pyi' :3 
name = data.getvalue("Name")
surname = data.getvalue("Surname")
description = data.getvalue("Description")

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student Details</title>")
print("</head>")
print("<body>")
print("<h1>{} {}</h1>".format(name,surname))
print("<p>{}</p>".format(description))
print("<a href=\"capturestudent.html\">Back</a>")
print("</body>")
print("</html>")
