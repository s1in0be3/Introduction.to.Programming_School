#! python3
# script called CalculateVolume.py.
#print()

# An engineer wants to calculate the volume of a rectangular tank.
# The program needs to request these 3 values as input from the user and store them in 3 different variables.
# Using these 3 variables, calculate the volume of the tank and store it in a fourth variable.
# The engineer has learned from experience that measurements and calculations are always a bit short of the volume the
# tank can store, because of the way the plastic tank expands when filled, so he requires that the script increase the
# calculated volume of the tank by 1% before displaying the resulting volume to the user.


#Volume of a Rectangle Box = Length x Breadth x Height
#Percentage = Value1 / Value2 = ? * 100

a, b, c = input("Enter Length: "), input("Enter Breadth: "), input("Enter Height: ")
#print ()

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
#print()
