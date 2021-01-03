#! python3
#MODULE 1, PRAX 3
# script called CalculateVolume.py.
#print()

# An engineer wants to calculate the volume of a rectangular tank.
# The program needs to request these 3 values as input from the user and store them in 3 different variables.
# Using these 3 variables, calculate the volume of the tank and store it in a fourth variable.
# The engineer has learned from experience that measurements and calculations are always a bit short of the
# volume the tank can store, because of the way the plastic tank expands when filled, so he requires that the
# script increase the calculated volume of the tank by 1% before displaying the resulting volume to the user.


#Volume of a Rectangle Box = Length x Breadth x Height
#Percentage = Value1 / Value2 = ? * 100

a, b, c = input("Enter Length: "), input("Enter Breadth: "), input("Enter Height: ")
print ()

type(a)
a = int(a)
print ()

type(a)
b = int(a)
print ()

type(a)
c = int(a)
print ()

d=(a) * (b) * (c)
e=(a / b / c)
f=e
g=f*100
h=g
i=d + h
j=i
k=i/100
l=k

#print("Volume",d)
#print("Percentage",g)
#print("The Volume and the 1% increase",k)

print("Volume of this particular tank =", k, end="")
print()
print()

#FASIT:
#length = float(input("Please enter a length: "))
#width = float(input("Please enter a width: "))
#height = float(input("Please enter a height: "))

#volume = (length * width * height) * 101 / 100
#print("Volume: ", volume)
#print()
#print()


#script called TimeCalculation.py.
#print()
#A manager has requested that you write a script that allows him to enter a value representing the number of
# minutes one of his employees has worked in a month. He wants the script to use the number of minutes to
# calculate the number of days worked in the month, the number of hours left over (not adding up to a full
# working day) and the number of minutes left over (not adding up to a full hour). For the sake of this
# calculation, a working day consists of 8 hours. Once calculated, display the resulting calculation in the
# following format: working days:hours:minutes.


#FASIT:
minutes = int(input("Please enter the number of (whole) minutes worked this month: "))
hours = int(minutes / 60)
minutes = int(minutes % 60)
days = int(hours / 8)
hours = int(hours % 8)
print("{0}:{1}:{2}".format(days, hours, minutes))
print()
#print()
#print()


#script called PizzaShop.py.
#print()

#The owner of the pizza shop has asked you to write a script that allows a customer to calculate the
# cost of a pizza. He has asked you to make the following options available to the customer:
#print()
#•	Pizza base (Customer must choose 1): Thick (Kr 10) or Thin (Kr 5)
#•	Pizza size (Customer must choose 1): Small (Kr 30), Medium (Kr 40) or Large (Kr 50)
#•	Basic sauce (Customer must choose 1): Tomato (Kr 5) or Barbecue (Kr 10)
#•	Toppings (Customer may choose any or none): Cheese (Kr 5), Mushrooms (Kr 3), Avocado (Kr 7), Pineapple (Kr 5), Bacon (Kr 7), Chicken (Kr 7) or Fish (Kr 6).
#print()
#If a specific item is selected display the item and its price on the screen.
# At the bottom (the last line) of the display present the customer with the total of the purchase.
#print()

#FASIT:
Total = 0

print("Select a pizza base type: ")
print("1.  Thick")
print("2.  Thin")
Base = int(input("Base selection: "))
BaseLine = ""
if Base == 1:
    BaseLine = "{0}Kr{1}".format("Thick base".ljust(20, " "), "10".rjust(5, " "))
    Total += 10
elif Base == 2:
    BaseLine = "{0}Kr{1}".format("Thin base".ljust(20, " "), "5".rjust(5, " "))
    Total += 5

print("Select a pizza size: ")
print("1.  Small")
print("2.  Medium")
print("3.  Large")
Size = int(input("Size selection: "))
SizeLine = ""
if Size == 1:
    SizeLine = "{0}Kr{1}".format("Small".ljust(20, " "), "30".rjust(5, " "))
    Total += 30
elif Size == 2:
    SizeLine = "{0}Kr{1}".format("Medium".ljust(20, " "), "40".rjust(5, " "))
    Total += 40
elif Size == 3:
    SizeLine = "{0}Kr{1}".format("Large".ljust(20, " "), "50".rjust(5, " "))
    Total += 50

print("Select a pizza sauce: ")
print("1.  Tomato")
print("2.  Barbecue")
Sauce = int(input("Sauce selection: "))
SauceLine = ""
if Sauce == 1:
    SauceLine = "{0}Kr{1}".format("Tomato sauce".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
elif Sauce == 2:
    SauceLine = "{0}Kr{1}".format("Barbecue sauce".ljust(20, " "), "10".rjust(5, " "))
    Total += 10

Toppings = ""
result = input("Would you like to add Cheese? (y or n): ")
if result == "y":
    Toppings += "{0}Kr{1}".format("Cheese".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
result = input("Would you like to add Mushrooms? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Mushrooms".ljust(20, " "), "3".rjust(5, " "))
    Total += 3
result = input("Would you like to add Avocado? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Avocado".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Pineapple? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Pineapple".ljust(20, " "), "5".rjust(5, " "))
    Total += 5
result = input("Would you like to add Bacon? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Bacon".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Chicken? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Chicken".ljust(20, " "), "7".rjust(5, " "))
    Total += 7
result = input("Would you like to add Fish? (y or n): ")
if result == "y":
    if len(Toppings) > 0:
        Toppings += "\n"
    Toppings += "{0}Kr{1}".format("Fish".ljust(20, " "), "6".rjust(5, " "))
    Total += 6

print()
print(BaseLine)
print(SizeLine)
print(SauceLine)
print(Toppings)
print("-" * 27)
print("{0}Kr{1}".format("Total".ljust(20, " "), str(Total).rjust(5, " ")))
#print()
#print()
#print()
