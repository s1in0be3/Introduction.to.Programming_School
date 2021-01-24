import cgi


data = cgi.FieldStorage()
studentnumber = data.getvalue("studentnumber")

name = "Not"
surname = "found"
description = "This student could not be found."

if studentnumber == "1":
	name = "John"
	surname = "Doe"
	description = "John is a very hard-working student."

if studentnumber == "2":
	name = "Jane"
	surname = "Doe"
	description = "Jane is our best student."

if studentnumber == "3":
	name = "Jim"
	surname = "Doe"
	description = "Jim needs to work harder."


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<style>")
print("<body {background-color: MistyRose;}>")
print("</style>")
print("<body>")
print("<h1>{} {}</h1>".format(name, surname))
print("<p>{}</p>".format(description))
print("<a href=\"student.list.html\">Back to Student List</a>")
print("<br>")
print("<a href=\"index.html\">Back to Homepage</a>")
print("</body>")
print("</html>")
