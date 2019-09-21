import numpy as np
import csv
import matplotlib.pyplot as plt
import p_ml_03

Xy = []
with open("winequality-red.csv") as fp:
    for row in csv.reader(fp, delimiter = ";"):         # 1行ごとに対象csvデータをリストに追加  
        Xy.append(row)
Xy = np.array(Xy[1:], dtype = np.float64)               # 0行目が文字列なので配列とする際に無視する([:1]で1行目以降の行を配列化)、文字列を数値に変換

np.random.seed(0)
np.random.shuffle(Xy)                                   # 行列Xyの行の順番をランダムに並び替える
train_X = Xy[:-1000, :-1]
train_y = Xy[:-1000, -1]
test_X = Xy[-1000:, :-1]
test_y = Xy[-1000:, -1]

model = p_ml_03.LinearRegression()
model.fit(train_X, train_y)

y = model.predict(test_X)

print("answer and prediction")
for i in range(100):
    print("answer = {:1.0f}\tprediction = {:5.3f}".format(test_y[i], y[i]))
print()
print("RMSE:", np.sqrt(((test_y - y)**2).mean()))

# 以下改造部分
axis_x = y
axis_y = y

for i in range(100):
    plt.scatter(test_y[i], y[i], color = "k")
    plt.plot(axis_x, axis_y, color = "r")
plt.show()