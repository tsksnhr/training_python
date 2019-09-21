with open("output.txt", "w") as f1:
    with open("sample.txt", "r") as f2:
        for line in f2:
            #print(line, end="", file=f1)
            print(line, file=f1)