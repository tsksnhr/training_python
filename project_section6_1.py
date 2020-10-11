#! python3
# パスワード管理プログラム

# モジュールインポート
import sys
import pyperclip

# dictionary
PASSWORD = {"email": "emailemailemailemailemailemail",
            "blog": "blogblogblogblogblogblogblogblog",
            "luggage": "12345"}

if len(sys.argv) < 2:
    print("How to use: project_section6.py")
    print("copy PASSWORD to a clipboard")
    sys.exit()

# 最初のコマンドライン引数がアカウント名
account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print(account + "'s password is copied to a clipboard.")
else:
    print(account + "is nothing.")

# 表示用に待ち時間
input()