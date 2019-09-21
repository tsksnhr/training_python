import random

stock = 13
print('在庫数は', stock, '個です', sep = '')

deliverly = random.choice([0, 10, 20])
print('配達数は', deliverly, '個です', sep = '')

new_stock = stock + deliverly
print('最終在庫数は', new_stock, '個です', sep = '')

if new_stock <  20:
    print('20個注文する')
elif 20 <= new_stock < 30:
    print('10個注文する')
else:
    print('注文しない')