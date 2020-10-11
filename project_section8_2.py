#! python3
# multi-clip board
# sys.argv[1] == "save": clipboard-text is copied with key(sys.argv[2])
# sys.argv[1] == "list": get keyword-list
# sys.argv[1] == valid keyword: get sentences to a clipboard

import sys
import pyperclip
import shelve
import os

if os.path.exists(".\\project8_2") == False:
    os.makedirs(".\\project8_2")

file_path = os.path.join(".", "project8_2", "mcb")
mcb_shelves = shelve.open(file_path)

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelves[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelves.keys())))
    elif sys.argv[1].lower() in mcb_shelves:
        pyperclip.copy(str(mcb_shelves[sys.argv[1].lower()]))

mcb_shelves.close()

# End Of File