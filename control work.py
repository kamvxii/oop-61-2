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
    @property
    def full_info(self):
        return self._balance
    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self, level):
        return self._balance - level


kama=BankAccount("Kama", 100000, "Kama123", "Mbank")
print(kama.get_bank_name())



#4task
class Test:
    def __init__(self, name, level, balance):
        self.name = name
        self.level = level
        self.balance = balance


    def __str__(self):
        return f"{self.name} | Баланс: {self.balance} SOM"

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level
    def __add__(self, other):
        return self.name + other.name
print(Test("Kama", 100, "Kama123"))



#5 task
from abc import ABC, abstractmethod

class SmsService(ABC):

    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        code = "1234"
        return f"<text>Код: {code}</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        code = "1234"
        return {
            "text": f"Код: {code}",
            "phone": phone
        }



kg = KGSms()
ru = RUSms()

print(kg.send_otp("+996500000000"))
print(ru.send_otp("+79990000000"))


