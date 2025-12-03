# 簡易RPGバトルシミュレーター
import random

class Player:

    hp = 100

    def __init__(self, name):
        self.name = name
    
    def attack(self, target):
        strength = random.randrange(5, 20)

        if target.hp - strength < 0:
            print(f"{self.name: >6}は{target.name: >6}に{strength}のダメージを与えた! {target.name: >6}: HP{target.hp} => 0")
        else:
            print(f"{self.name: >6}は{target.name: >6}に{strength}のダメージを与えた! {target.name: >6}: HP{target.hp} => {target.hp - strength}")

        target.hp -= strength
    
    def print_spec(self):
        print(f"NAME: {self.name: >6}\nHP: {self.hp}")


class Enemy:

    hp = 100

    def __init__(self, name):
        self.name = name

    def attack(self, target):
        strength = random.randrange(5, 20)
        
        if target.hp - strength < 0:
            print(f"{self.name: >6}は{target.name: >6}に{strength}のダメージを与えた! {target.name: >6}: HP{target.hp} => 0")
        else:
            print(f"{self.name: >6}は{target.name: >6}に{strength}のダメージを与えた! {target.name: >6}: HP{target.hp} => {target.hp - strength}")

        target.hp -= strength

    def print_spec(self):
        print(f"NAME: {self.name: >6}\nHP: {self.hp}")


player_A = Player("yamada")
monstar = Enemy("Slime")

while True:
    player_A.attack(monstar)
    if monstar.hp <= 0:
        print(f"{player_A.name: >6}は{monstar.name: >6}を倒した")
        break

    monstar.attack(player_A)
    if player_A.hp <= 0:
        print(f"{player_A.name: >6}は{monstar.name: >6}に倒された")
        break

    print()

print()
player_A.print_spec()
monstar.print_spec()