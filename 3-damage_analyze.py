# numpy を使って、平均50、標準偏差10の正規分布に従うランダムな数値を「1000回分」生成し、配列（array）にする（＝1000回の攻撃ダメージログと仮定）。
# その1000回の攻撃の中で、「最大ダメージ」と「最小ダメージ」を表示する。
# 「ダメージが60以上」だった回数（クリティカル数）をカウントして表示する。
# 全ダメージの「平均値」を表示する。

import numpy as np
damages = np.random.normal(loc=50, scale=10, size=1000)
# 平均50, 標準偏差10, のランダムな数値1000個

print(f"MAX: {np.max(damages)}\nMIN: {np.min(damages)}")

# criticals = damages[damages > 60]
# print(f"CRITICAL: {len(criticals)}")
# ↑はメモリを食うのでTrueの数だけ数えるコード1行に変える
count = np.sum(damages > 60)
print(f"CRITICAL: {count}")

print(f"AVERAGE: {np.mean(damages)}")