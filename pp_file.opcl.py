# challenge 01

import os
import csv

"""
fpath = os.path.join("C:\\", "Users", "chest", "Desktop", "hoge.csv")
print(fpath)

if os.path.exists(fpath):
    with open(fpath, "r", encoding = "utf-8") as fp:
        for row in fp:
            print(row.rstrip())

else:
    print("There's no file.")
"""

# challenge 02

"""
ans_list = []
iter = 0
max_iter = 10
dit = 0

while ((iter < max_iter) and (dit != 1)):
    print("dit = {}".format(dit))
    ans_list.append(input("What's your favorite foods?: "))
    iter = iter + 1

    dit = int(input("Finish? Yes:1 No:2 "))

fpath = os.path.join("C:\\", "Users", "chest", "Desktop", "foo.csv")
print(fpath)

if os.path.exists(fpath):
    with open(fpath, "w", encoding = "utf-8") as fp:
        W_buf = csv.writer(fp, delimiter = ",")
        W_buf.writerow(ans_list)

else:
    print("There's no file.")
"""

# challenge 03

data_list = [["a", "b", "c"], ["d", "e", "f"], ["g", "h","i"]]

fpath = os.path.join("C:\\", "Users", "chest", "Desktop", "foo.csv")

if os.path.exists(fpath):
    with open(fpath, "w", encoding = "utf-8") as fp:
        w_buf = csv.writer(fp, delimiter = ",")
        w_buf.writerow(data_list[0])
        w_buf.writerow(data_list[1])
        w_buf.writerow(data_list[2])

else:
    print("file does not exist.")
        