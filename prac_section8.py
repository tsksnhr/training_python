# 8.10.1

# module import
import os
import sys
import pyperclip
import shelve

# make directory
if os.path.exists(".\\project8_2") == False:
    os.makedirs(".\\project8_2")

# get path
file_path = os.path.join(".", "project8_2", "mcb_ad")
mcb_shelf = shelve.open(file_path)

# command line argument
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "del":
        mcb_shelf.pop(sys.argv[2])
        # del mcb_shelf[sys.argv[2]]
    else:
        print("invalid arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] == "delall":
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(str(mcb_shelf[sys.argv[1]]))

mcb_shelf.close()

# End Of File