for number in range(31):

    if number % 15 == 0:
        print("fuzzbizz")
    elif number % 3 == 0:
        print("fuzz")
    elif number % 5 == 0:
        print("bizz")
    else:
        print(number)
