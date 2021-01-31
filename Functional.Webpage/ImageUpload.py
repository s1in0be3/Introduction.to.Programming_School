import cgi, os

data = cgi.FieldStorage()
upload = data["imagefile"]
filename = os.path.basename(upload.filename)

with open(filename, "wb") as copy:
	copy.write(upload.file.read())

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(filename))
print("<img src=\"{}\"/><br/><br/>".format(filename))
print("<a href=\"imageupload.html\">Back</a>")
print("</body>")
print("</html>")