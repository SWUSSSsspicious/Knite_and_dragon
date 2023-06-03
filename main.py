from random import randint
class Hero():
    def __init__ (self, name, health, armor, power):
        self.name=name
        self.health=health
        self.armor=armor
        self.power=power
        self.new=True
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
    def check_alive(self):
        if self.health<=0:
            return True
        else:
            return False
    def strike(self, enemy):
        enemy.armor-=self.power
        if enemy.armor<0:
            enemy.health+=enemy.armor
            enemy.armor=0


class Warrior(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный воин', self.name)
            self.new=False
        else:
            print('Снова появляется воинственный', self.name)
    def attack(self, enemy):
        print(self.name , 'бесстрашно набрасывается на', enemy.name)

class Dragon(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! С неба спускается свирепый дракон', self.name)
            self.new=False
        else:
            print('И вновь перед нами разъярённый дракон', self.name)
    def attack(self, enemy):
        print(self.name, 'направляет поток смертельного огня на', enemy.name)


warrior_1=Warrior('Сержио', 10, 15, 12)
warrior_2=Warrior('Питер', 20, 10, 9)
dragon_1=Dragon('Дрогон', 12, 25, 13)
dragon_2=Dragon('Визерион', 12, 20, 8)
hero=Warrior('Ричард', 70, 30, 20)
fighters=[hero, warrior_1, warrior_2,dragon_1,dragon_2]
permition=input('Ты стоишь у входа в лес, полный смертельных опасностей. Готов ли ты войти внутрь и сразиться с врагами (да/нет)? \n').lower()
print('\n ***Да начнётся битва!*** \n')
while permition=='да':
    count=randint(1, len(fighters)-1)
    if len(fighters)==2:
        count=1
    fighters[count].hello()
    fighters[count].print_info()
    permition_2=input('Вступить в бой (да/нет)?').lower()
    end=False
    while permition_2=='да':
        count_=randint(0,1)
        if count_==0:
            fighters[0].attack(fighters[count])
            fighters[0].strike(fighters[count])
        else:
            fighters[count].attack(fighters[0])
            fighters[count].strike(fighters[0])
        print('Результат схватки для', fighters[0].name)
        fighters[0].print_info()
        print('Результат схватки для', fighters[count].name)
        fighters[count].print_info()
        print('---')
        if fighters[count].health<=0 and fighters[count].armor==0:
            print(fighters[count].name, 'погиб от руки', fighters[0].name, '\n')
            fighters.remove(fighters[count])
            break
        if fighters[0].health<=0:
            print('Храбрый рыцарь',fighters[0].name,'погиб в бою с врагами')
            end=True
            break
        elif len(fighters)==1 and fighters[0]==hero:
            print('Храбрый рыцарь', hero.name, 'победил всех врагов!')
            end=True
            break
        permition_2=input('Вступить в бой (да/нет)?').lower()
    if end:
        break
print('Тут и сказочке конец')