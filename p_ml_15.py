import numpy as np
import csv
import p_ml_14_Lasso          # Lasso regression

Xy = []

with open("winequality-red.csv") as fp:
    for row in csv.reader(fp, delimiter = ";"):
        Xy.append(row)

Xy = np.array(Xy[1:], dtype = np.float64)

np.random.seed(0)
np.random.shuffle(Xy)

# ホールドアウト法
train_X = Xy[:-1000, :-1]
train_y = Xy[:-1000, -1]
test_X = Xy[-1000:, :-1]
test_y = Xy[-1000:, -1]

#print("--train_X--")
#print(train_X)
#print("--train_y--")
#print(train_y)
#print("--test_X")
#print(test_X)

for lambda_ in [1, 0.1, 0.01]:
    model = p_ml_14_Lasso.Lasso(lambda_)
    model.fit(train_X, train_y)
    y = model.predict(test_X)

    print("---Lambda = {}".format(lambda_))
    print("Coefficients:")
    print(model.w_)
    mse = ((y - test_y)**2).mean()
    print("mse = {:.3f}".format(mse))
