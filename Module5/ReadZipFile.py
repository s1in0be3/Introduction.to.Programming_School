#This code need spesification from your own computer.
#This file is called "ZipFile.py" in the project.
import zipfile

with zipfile.Zipfile("myarchive.zip", r) as zipfile:
    for current in zipfile.namelist():
        print(current)
