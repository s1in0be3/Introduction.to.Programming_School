import zipfile

with zipfile.Zipfile("myarchive.zip", r) as zipfile:
    for current in zipfile.namelist():
        print(current)
