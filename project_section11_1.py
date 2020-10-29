#! python3

# import module
import os
import sys
import pyperclip
import webbrowser

if len(sys.argv) > 1:
    str_address = " ".join(sys.argv[1:])
else:
    str_address = pyperclip.paste()

webbrowser.open("https://www.google.co.jp/maps/place/" + str_address)

# End of File