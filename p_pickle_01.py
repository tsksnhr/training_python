# pickleというモジュールはオブジェクトの中身をファイルに書き出し、必要に応じてそれを読み込んで元のオブジェクトを復元したいときに使う

from datetime import date
import pickle

x = date(2018,8,25)

# pickle形式で書き込むにはdump()を使用する
with open("today.pkl", "wb") as f:
    pickle.dump(x, f, -1)

# pickle形式のファイルを読み込むにはload()を使用する
with open("today.pkl", "rb") as f:
    y = pickle.load(f)

print(x)
print(f)
print(y)