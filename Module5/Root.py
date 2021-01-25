import os

root_path = "C:\\Users\'username'\PycharmProjects"
print(root_path)
print()

root_path = os.path.join("c:", "users")
print(root_path)
print()

root_path = os.getcwd()
print(root_path)
print()

os.chdir("\\users")
root_path = os.getcwd()
print(root_path)
print()
