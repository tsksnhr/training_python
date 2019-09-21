for i in range(11):
    print(i)

print("---")

number_list = [number for number in range(11)]
print(number_list)
for column in number_list:
    print(column)

print("---")

string = "abcdefg"
for character in string:
    print(character)

print("---")

string_list = ["*"+ character + "*" for character in string]
print(string_list)
print(list(string))