import numpy as np

print(np.random.rand())                                 # 乱数生成(0~1)
print("")
print(np.random.rand(4, 5))                             # 乱数生成(4行5列の2次元配列として)
print("")
print(np.random.rand(6))                                # 乱数生成(サイズ6の1次元配列として)
print("")
print(np.random.randint(10))                            # 乱数生成(10以下の整数ひとつ)
print("")
print(np.random.randint(10, 20))                        # 乱数生成(10～20の整数ひとつ、ただし20は含まない)
print("")
print(np.random.randint(10, 20, size = (5, 5)))         # 乱数生成(10～20の整数を5行5列の2次元配列として)
