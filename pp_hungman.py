def hungman(word):

    stages = ["",
              "________",
              "|       ",
              "|   |   ",
              "|   O   ",
              "   /|\\  ",
              "   / \\  ",
              "_________"]
    
    ans = list(word)
    ans_container = ["_"]*len(word)
    miss = 0
    ditermine = False 

    print("Hungman, start!")

    while ditermine != True:

        ans_buf = input("Predict answer word: ")

        if ans_buf in ans:
            position = ans.index(ans_buf)
            ans_container[position] = ans_buf
            ans[position] = "$"
            print(ans_container)
        else:
            miss += 1
            print("\n".join(stages[0:miss]))
        
        if ans == ["$"]*len(word):
            ditermine = True
            print("The word is {}, You win!".format(word))
        elif miss == len(stages):
            ditermine = True
            print("The word is {}, You lose!".format(word))
        else:
            ditermine = False

hungman("apple")
