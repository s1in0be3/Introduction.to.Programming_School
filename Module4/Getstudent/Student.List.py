import cgi


data = cgi.FieldStorage()
studentnumber = data.getvalue("studentnumber")

name = "Not"
surname = "found"
description = "This student could not be found."

if studentnumber == "1":
	name = "Fredrik"
	surname = "Boe"
	description = "Fredrik is a very hard-working student."

if studentnumber == "2":
	name = "Johanne"
	surname = "Dew"
	description = "Johanne is our best student."

if studentnumber == "3":
	name = "James"
	surname = "Doen"
	description = "James needs to work harder."


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print("<h1>{} {}</h1>".format(name, surname))
print("<p>{}</p>".format(description))
print("<a href=\"Student.List.html\">Back</a>")
print("</body>")
print("</html>")
