# numpyで作った正規表現データをヒストグラムにする(3と同じく攻撃力を想定する)

import numpy as np
import matplotlib.pyplot as plt

datas = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(x=datas, bins=30, alpha=0.7, label="Attack Damage") # 改善点：alphaで少し透けさせる、ラベルを付ける

plt.title("Damage Distribution") # 改善点：タイトル追加
plt.xlabel("Damages")
plt.ylabel("Count")

# クリティカルライン
plt.axvline(x=60, color="red", linestyle="--") # 改善点：点線にする

plt.legend() # 改善点：凡例を表示
plt.show()