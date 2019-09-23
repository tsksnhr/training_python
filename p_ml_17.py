import numpy as np
import p_ml_16_logisticReg
import csv

n_test = 100
X = []
y = []

with open("wdbc.data") as fp:
    for row in csv.reader(fp):
        if row[1] == "B":
            y.append(0)
        else:
            y.append(1)
        X.append(row[2:])

y = np.array(y, dtype = np.float64)
X = np.array(X, dtype = np.float64)

y_train = y[:-n_test]
X_train = X[:-n_test]

y_test = y[-n_test:]
X_test = X[-n_test:]

model = p_ml_16_logisticReg.LogisticRegression(tol = 0.01)
model.fit(X_train, y_train)

y_predict = model.predict(X_test)
#n_hits = (y_test == y_train).sum()          #boolオブジェクトはsumダメって言われる・・・行列のサイズが違うと計算できない？
n_hits = (y_test == y_predict).sum()       #こっちは上手くいく
print("Acuuracy: {}/{} = {}".format(n_hits, n_test, (n_hits/n_test)))

#調査
print("y_test.shape = {}".format(y_test.shape))
print("y_train.shape = {}".format(y_train.shape))
print("y_predict.shape = {}".format(y_predict.shape))
