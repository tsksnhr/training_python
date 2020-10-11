#! python3
# 文書から電話番号とメールアドレスを抜き出すプログラム

# module import
import re
import pyperclip

# regex for phone number
phone_regex = re.compile(r"""
    (
    (\d{3}|\(\d{3}\))?                  # 1
    (\s|-|\.)?                          # 2
    (\d{3})                             # 3
    (\s|-|\.)                           # 4
    (\d{4})                             # 5
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?     # 6(7 8)
    )
    """, re.VERBOSE)

# regex for e-mail address
email_regex = re.compile(r"""
    (
    [a-zA-Z0-9_%+-.]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )
    """, re.VERBOSE)

# get sentences from a clipboard
cl_text = pyperclip.paste()
matches = []

# search phone number
for grp in phone_regex.findall(cl_text):                # タプルのリストが返ってくる
    phone_num = "-".join([grp[1], grp[3], grp[5]])      # join()に渡すのはリストなので、タプルをリスト化して渡す

    if grp[8] != "":
        phone_num += " x" + grp[8]

    matches.append(phone_num)

# search e-mail address
for grp in email_regex.findall(cl_text):
    matches.append(grp[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("data copied.")
    print("\n".join(matches))
    input()
else:
    print("data not found.")
    input()
