def meow():
    print("meow!")

def main():
    print("main function")
    meow()

# 直接実行された時だけmain()が呼ばれる
if __name__ == "__main__":
    main() 