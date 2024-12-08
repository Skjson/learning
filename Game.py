from gc import get_stats

from pick import pick
import random
import time
import threading

class Character(object):
    def __init__(self, name, HP=50, damage=10, wisdom=50, money=100, stamina = 100, xp = 0):
        self.name = name
        self.HP = HP
        self.max_HP = HP
        self.damage = damage
        self.wisdom = wisdom
        self.money = money
        self.stamina = stamina
        self.xp = xp

    def run_regeneration(self):
        t = threading.Thread(target=self.regeneration_loop)
        t.start()
    def regeneration_loop(self):
        while True:
            self.regeneration()
            time.sleep(1)


    def Heal(self, amount):
        if amount > 0:
            self.HP = min(self.max_HP, self.HP + amount)
    def regeneration(self):
        if self.HP < self.max_HP:
            self.HP = min(self.max_HP, self.HP + 1)
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
            enemy_HP = 120
            enemy_damage = 30
        while self.HP > 0 and enemy_HP > 0:
            enemy_HP -= self.damage
            self.HP -= enemy_damage
        if self.HP > 0:
            self.money+=10
            self.xp+=11
        else:
            print("Здесь ты проиграл!")

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


characterName()
character_1.run_regeneration()

enemies = {
    0: lambda character: character.Fight('knight'),
    1: lambda character: character.Fight('archer'),
    2: lambda character: character.Fight('BOSS'),
}
actions = {
    1: lambda character: character.Training(),
    2: lambda character: character.Studying(),
    3: lambda character: character.Heal(30),
    # 4: lambda character: character.Fight('knight'),
    5: lambda character: character.Fight('BOSS')
}
# characteristics = {
#     0: lambda character: print('Твое максимальное ХП сейчас:', character.max_HP),
#     2: lambda character: print('Твое максимальный урон сейчас:', character.damage),
#     3: lambda character: print('Твоя мудрость:',character.wisdom),
#     4: lambda character: print('Твоя энергия:',character.stamina),
#     5: lambda character: print('Твои деньги:',character.money)
# }
def main():
    while True:
        title = 'Выбери действие своего персонажа '
        options = ['Показать характеристики','Качаться', 'Учиться', 'Лечиться', 'Сражаться','Сражаться c БОССОМ', ]
        option, index = pick(options, title, indicator="->")
        if index == 0:
            title1 = 'Твои характеристики'
            options = [f'Здоровье: {character_1.HP}/{character_1.max_HP}',f'Урон: {character_1.damage}',
                        f'Опыт: {character_1.xp}',''f'Энергия: {character_1.stamina}/100', f'Деньги: {character_1.money}']
            pick(options, title1, indicator="")
        elif index == 1:
            title = 'Ты прокачался'
            pick([''],title,indicator="")
            actions[index](character_1)
        elif index == 2:
            title = 'Ты поучился!'
            pick([''],title,indicator="")
            actions[index](character_1)
        elif index == 3:
            title = 'Ты подлечился на 30 единиц!'
            pick([''],title,indicator="")
            actions[index](character_1)
        elif index == 4:
            title = 'Выбери с кем сразишься!'
            options = [f'Рыцарь (50 хп / 10 урона)', f'Лучник (40 хп / 20 урона)', 'Назад' ]
            option, index = pick(options,title,indicator="->")
            if index != 2:
                enemies[index](character_1)
            else:
                continue
        elif index == 5:
            title = 'Время сражаться c БОССОМ! (120 хп / 40 урона'
            options = ['В БОЙ!', 'Назад']
            option, ind = pick([''], title, indicator="->")
            if index == 2:
                enemies[index](character_1)
            else:
                continue







if __name__ == "__main__":
    main()
