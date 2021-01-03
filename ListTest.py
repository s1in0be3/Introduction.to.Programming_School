#! python3
#How to make lists:
#print()

the_list = list()

for current in range(0, 3):
    the_list.append(input("Please enter a name: "))
#print()

#UNSORTED:
print("Unsorted: ", end="")
print(the_list)
#print()

#SORTED:
the_list.sort()
print("Sorted: ", end="")
print(the_list)
#print()

#Serch for, if found and if not found:
search = input("Enter a name to search for: ")

index = -1

for i in range(0, 3):
    if the_list[i] == search:
        index = i
        break

if index > -1:
    print(search, "was found at index", index, ".")
else:
    print("The name does not exist.")
#print()

#REVERSE THE LIST, SORTED:
the_list.reverse()
print("Sorted: ", end="")
print(the_list)

the_slice = the_list[0: int(len(the_list) / 2)]

print("Slice: ", end="")
print(the_slice)
#print()

the_list.append(input("Please enter a name: "))

print("Final: ", end="")
print(the_list)
#print()
#print()
#print()
#print()
#print()
#print()
#LIST: ADDON AND VIEW SHARED ITEMS ON LIST:
my_set = {"burger", "pizza", "burrito", "taco", "hot dog"}
friend_set = {"burger", "fried chicken", "pizza", "wrap", "ramen"}
my_set.add("nachos")
print("Shared: ", my_set.intersection(friend_set))
#print()
