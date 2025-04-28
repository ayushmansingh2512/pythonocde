import os
# specify the directory you nwant a list
diractory_path = '/'

contents = os.listdir(diractory_path)

for item in contents:
    print(item)