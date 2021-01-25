#This code need spesification from your own computer.
import zipfile

with zipfile.Zipfile("myarchive.zip", r) as zipfile:
    for current in zipfile.namelist():
        print(current)
