# challenge 01

string = "カミュ"

for dummy in range(3):
    print(string[dummy])

# challenge 02

str_1 = input("string?: ")
str_2 = input("string?: ")

print("string1 is {}, string2 is {}".format(str_1, str_2))

# challenge 03

str_3 = "that man was born in 1992."
print(str_3.capitalize())

# challenge 04

str_4 = "Where? Who? When?"
print(str_4.split(" "))

# challenge 05

str_5 = [" The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(str_5).strip().replace("fence ", "fence"))

# challenge 05

str_6 = "Hemingway"
print(str_6.index("e"))

# challenge 07
print("three"+"three"+"three")
print("three"*3)