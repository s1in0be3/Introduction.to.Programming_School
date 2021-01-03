#! python3
#1. Create a script called ListTest.
# The script is required to do the following:
#print()

#Request 10 names of friends from the user and save them in the list.
#print()
#Define a list
the_list = list()

for current in range(0, 10):
    the_list.append(input("Please enter a name: "))
#print()

print("Unsorted: ", end="")
print(the_list)
#print()

#c.	Sort the list.
#print()
the_list.sort()
print("Sorted: ", end="")
print(the_list)
#print()

#Ask the user for a name to search for.
search = input("Enter a name to search for: ")

index = -1

for i in range(0, 10):
    if the_list[i] == search:
        index = i
        break

#If the name exists in the list, display its index otherwise display the message “The name does not exist”.
if index > -1:
    print(search, "was found at index", index, ".")
else:
    print("The name does not exist.")
#print()

#Reverse the list.
the_list.reverse()
print("Sorted: ", end="")
print(the_list)

#Create a slice of the list consisting of the first half of the list entries.
#Display the contents of the slice.
the_slice = the_list[0: int(len(the_list) / 2)]

print("Slice: ", end="")
print(the_slice)
#print()

#Ask the user for one more name. Append the name to the end of the original list.
the_list.append(input("Please enter a new name to add on list: "))

print("Final: ", end="")

#Display the contents of the original list.
print(the_list)
print()
print()
#print()
#print()



#Create a script called SetTest. The script is required to do the following:
#Define a set

#Populate the set with the names of your 5 favourite fast foods (no user input required).
# Define a second set and populate it with the names of a friend’s 5 favourite fast foods (no user input required).
# Add another type of fast food to your set of favourite foods.
# Determine which favourite fast foods are shared by you and your friend and display these overlapped foods.

my_set = {"burger", "pizza", "burrito", "taco", "hot dog"}
friend_set = {"burger", "fried chicken", "pizza", "wrap", "ramen"}
my_set.add("nachos")
print("Shared: ", my_set.intersection(friend_set))
print()
print()
#print()
#print()
#print()
#print()
#print()
#print()
#Create a script called MyPhonebook. The script is required to do the following:
#print()
# Define a dictionary consisting of 5 business names and their associated phone numbers.
# The business name should be used as the key.
phonebook = {"Nikita AS": "222 33 222",
             "På Håret AS": "444 99 444",
             "Adam & Eva AS": "777 22 777",
             "Short Cut AS": "111 77 111",
             "Cutters AS": "333 88 333"}

print(phonebook)

# Request the name and number of another business from the user and add it to the dictionary.
# Ask the user to type in the name of a business.
# # If the business exists, display it’s phone number; otherwise display the message
# # “The business is not in the phonebook.”.

company_name = input("Enter a company name to be added to the list: ")
company_number = input("Enter the company's number: ")
phonebook[company_name] = company_number


search = input("Search for a  already existing company name: ")

if search in phonebook.keys():
    print(phonebook[search])
else:
    print("The company is not in the phonebook.")

# Display the entire dictionary (names and phone numbers).
print(phonebook)
# Display only the business names (no phone numbers).
print(phonebook.keys())
#print()