from pick import pick
import random
import time
import threading

class Character(object):
    def __init__(self, name, HP=50, damage=10, wisdom=50, money=100, stamina = 100):
        self.name = name
        self.HP = HP
        self.max_HP = HP
        self.damage = damage
        self.wisdom = wisdom
        self.money = money
        self.stamina = stamina

    def run_adventure_love(self):
        t = threading.Thread(target=self.adventure_love)
        t.start()
    def adventure_love(self):
        while True:
            self.passiveRecovery()
            time.sleep(1)


    def Heal(self, amount):
        if amount > 0:
            self.HP = min(self.max_HP, self.HP + amount)
    def passiveRecovery(self):
        if self.HP < self.max_HP:
            self.HP = min(self.max_HP, self.HP + 5)
        if self.stamina < 100:
            self.stamina = min(self.stamina + 1, 100)
    def Training(self):
        if self.stamina >0:
            self.stamina -= 5
            self.damage += random.randint(1,5)
            self.max_HP +=  random.randint(2,5)
        else:
            print("Не хватает энергии")
            pass

    def Studying(self):
        if self.stamina >0:
            self.wisdom +=random.randint(2,5)
            self.stamina -=5
        else:
            print("Не хватает энергии")
            pass

    def Fight(self, enemy_type):
        if enemy_type == 'knight':
            enemy_HP = 50
            enemy_damage = 10
        elif enemy_type == "archer":
            enemy_HP = 40
            enemy_damage = 20
        elif enemy_type == "BOSS":
            enemy_HP = 40
            enemy_damage = 20
        while self.HP > 0 and enemy_HP > 0:
            enemy_HP -= self.damage
            self.HP -= enemy_damage
        if self.HP > 0:
            print("Win")
            self.money+=10
        else:
            print("Lose")

class Stats(Character):
    def getStats(self):
        print(f"{self.HP}/{self.max_HP}, damage:{self.damage}, wisdom:{self.wisdom}, money:{self.money}, stamina:{self.stamina}")

class Shop(object):
    def __init__(self, id, name, cost, hp, dps, wisdom):
        pass


def characterName():
    global character_1
    name = input(f"Напиши имя для своего персонажа " + "\n")
    character_1 = Character(name)
    print(f"Вот характеристики твоего персонажа, {name} \n ")
    Stats.getStats(character_1)


characterName()

character_1.run_adventure_love()


actions = {
    0: lambda character: character.Training(),
    1: lambda character: character.Studying(),
    2: lambda character: character.Heal(10),
    3: lambda character: character.Fight('knight'),
    4: lambda character: character.Fight('BOSS')
}

def main():
    while True:
        title = 'Выбери действие своего персонажа '
        options = ['Качаться', 'Учиться', 'Лечиться', 'Сражаться','Сражаться c БОССОМ']
        option, index = pick(options, title)
        actions[index](character_1)
        Stats.getStats(character_1)
        input()

if __name__ == "__main__":
    main()
