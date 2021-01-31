import cgi

data = cgi.FieldStorage()

price = 0
pizza_size = data.getvalue("size")
pizza_base = data.getvalue("base")

if pizza_base == "Thin":
	if pizza_size == "Small":
		price = 30
	if pizza_size == "Medium":
		price = 50
	if pizza_size == "Large":
		price = 70
elif pizza_base == "Thick":
	if pizza_size == "Small":
		price = 34
	if pizza_size == "Medium":
		price = 57
	if pizza_size == "Large":
		price = 80
print()

toppings = "<li>"
price2 = 0

if data.getvalue("cheese"):
	toppings += "<li>" + data.getvalue("cheese") + ":  0.50</li>"
	price2 += 0.50

if data.getvalue("bacon"):
	toppings += "<li>bacon:  0.90</li>"
	price2 += 0.90

if data.getvalue("pineapple"):
	toppings += "<li>pineapple:  0.70</li>"
	price2 += 0.70

if data.getvalue("avocado"):
	toppings += "<li>avocado:  0.80</li>"
	price2 += 0.80

toppings += "</li>"
Total = price + price2

locations = data.getvalue("locations")
addresses = ""

if locations == "Home":
	addresses = "Home Street 1<br/>Hometown<br/>1234"

if locations == "Work":
	addresses = "Fatigue Road 55<br/>Tiredton<br/>4839"

print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza order</title>")
print("</head>")
print("<body>")
print("<h1>Your Pizza order is:</h1></br>")
print("You ordered a {0} {1} pizza, (and): {2} FOR {3:.2f} KR TOTAL.<br/><br/>".format(pizza_base, pizza_size, toppings, Total))
print("<h1>Pizza delivery location is:</h1>")
print("{0}" "{1}<br/><br/>".format(locations, addresses))
print("<a href=\"makeyourorderhere.html\">Back</a>")
print("</body>")
print("</html>")
#
# #
# import cgi
#
# data = cgi.FieldStorage()
#
# price = 0
# pizza_size = data.getvalue("size")
# pizza_base = data.getvalue("base")
#
# if pizza_base == "Thin":
# 	if pizza_size == "Small":
# 		price = 30
# 	if pizza_size == "Medium":
# 		price = 50
# 	if pizza_size == "Large":
# 		price = 70
# elif pizza_base == "Thick":
# 	if pizza_size == "Small":
# 		price = 34
# 	if pizza_size == "Medium":
# 		price = 57
# 	if pizza_size == "Large":
# 		price = 80
# print()
#
#
# print("<!DOCTYPE HTML>")
# print("<html>")
# print("<head>")
# print("<title>Pizza order</title>")
# print("</head>")
# print("<body>")
# print("<h1>Pizza order:</h1>")
# print("You ordered a {0} {1} base pizza at a price of {2:.2f}.<br/><br/>".format(pizza_size, pizza_base, price))
# print("</body>")
# print("</html>")
#
# toppings = "<ul>"
# price2 = 0
#
# if data.getvalue("cheese"):
# 	toppings += "<li>" + data.getvalue("cheese") + ":  0.50</li>"
# 	price2 += 0.50
#
# if data.getvalue("bacon"):
# 	toppings += "<li>bacon:  0.90</li>"
# 	price2 += 0.90
#
# if data.getvalue("pineapple"):
# 	toppings += "<li>pineapple:  0.70</li>"
# 	price2 += 0.70
#
# if data.getvalue("avocado"):
# 	toppings += "<li>avocado:  0.80</li>"
# 	price2 += 0.80
#
# toppings += "</ul>"
#
# print()
# print("<!DOCTYPE HTML>")
# print("<html>")
# print("<head>")
# print("<title>Pizza order</title>")
# print("</head>")
# print("<body>")
# print("<h1>List of toppings:</h1>")
# print(toppings)
# print("Price:  {0:.2f}<br/><br/>".format(price2))
# print("<a href=\"OrderPizzza.html\">Back</a>")
# print("</body>")
# print("</html>")
