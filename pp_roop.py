# challenge 01
"""
list_hoge = ["a", "b", "c", "d", "e"]

for column in list_hoge:
    print(column)
"""
# challenge 02
"""
for i in range(25,51):
    print(i)
"""
# challenge 03



# challenge 04
"""
ans_list = ["2", "3", "5", "7", "9", "11", "13", "17", "19"]

test = input("数字を入力してください: ")
print(test)

while(test != "q"):

    if test in ans_list:
        print("正解！")
        break
    else:
        print("残念！")
        test = input("数字を入力してもう一度チャレンジするか、qを押して終了してください: ")
"""

# challenge 05

list_a = [8, 19, 148, 4]
list_b = [9, 1, 33, 83]

for i in list_a:
    for j in list_b:
        print(i*j)
