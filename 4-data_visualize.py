# numpyで作った正規表現データをヒストグラムにする(3と同じく攻撃力を想定する)

import numpy as np
import matplotlib.pyplot as plt

datas = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(x=datas, bins=30)
plt.xlabel("Damages")
plt.ylabel("Count")
plt.axvline(x=60, color="red") # ここからクリティカルダメージ
plt.show()