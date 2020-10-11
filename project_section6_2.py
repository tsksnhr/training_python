#! python3
# クリップボードのテキスト各行に"*"を追加する

# module import
import pyperclip

# クリップボードから文章を取得
cl_text = pyperclip.paste()

# 文字列を改行で分割してリスト化し、"*"を追加
text_list = cl_text.split("\n")
for i in range(len(text_list)):
    text_list[i] = "*" + text_list[i]

# 文字列の再結合
cl_text = "\n".join(text_list)

# クリップボードに文章をコピー
pyperclip.copy(cl_text)
