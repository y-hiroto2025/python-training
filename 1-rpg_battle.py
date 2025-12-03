# 簡易RPGバトルシミュレーター
import random

# 改善点：DRY。同じものは繰り返してはいけない。複数のクラスが共通のものを持つならば、継承を利用する。

# base class
class Character:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
        self.max_hp = hp 
    
    def attack(self, target):
        # targetに5~20のダメージを与える
        # 改善点：5~20ならば、randrange(5, 21) or randint(5, 20)
        damage = random.randint(5, 20)

        target.hp -= damage

        # 改善点：max関数を使って、HPが0にならないように補正
        target.hp = max(target.hp, 0)

        print(f"{self.name: >6} の攻撃  {target.name: >6} に {damage} のダメージ")
        print(f"    {target.name: >6} HP: {target.hp}/{target.max_hp}")

        # 改善点：生存判定の関数を作って、倒れたかどうかの判定に使う
    def is_alive(self):
        return self.hp > 0


# sub class
# 内容はまた今度書く
class Player(Character):
    pass

class Enemy(Character):
    pass


player = Player("Yamada")
monster = Enemy("Slime")

print("--- BATTLE START ---")

while True:
    # プレイヤーのターン
    player.attack(monster)
    if not monster.is_alive():
        print(f"\n  >>{player.name}は{monster.name}を倒した")
        break

    # モンスターのターン
    monster.attack(player)
    if not player.is_alive():
        print(f"\n  >>{player.name}は{monster.name}に倒された")
        break

    print("=" * 40)
