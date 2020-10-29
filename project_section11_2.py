#! python3

# module import
import requests

resobj = requests.get("https://shoutoutfest.com/jp/cutiemutie520.php")

try:
    resobj.raise_for_status()
    test_file = open("test.txt", "wb")      # making file by write() method

    for chunk in resobj.iter_content(100000):
        test_file.write(chunk)

    test_file.close()

except Exception as ext:
    print("error occured. {}".format(ext))

# End Of File