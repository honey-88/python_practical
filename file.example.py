#create folder

import os

if os.path.exists(r"C:\Users\Honey\Documents\GitHub\python_practical\MYFOLDER"):
    print("folder is already exist")
else:
    os.mkdir(r"C:\Users\Honey\Documents\GitHub\python_practical\MYFOLDER")
    print("created folder")