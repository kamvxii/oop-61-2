#1 task
class Hero:
    def __init__(self,name,lvl,hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f"{self.name} готов к бою!")
sasuke = Hero("Sasuke", 5, 120)
sasuke.action()
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")
friren=MageHero("Friren", 5, 120,9)
friren.action()
class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name,lvl,mp,hp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")
emilia=WarriorHero("Emilia", 5, 120,89)
emilia.action()


#3task
class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password