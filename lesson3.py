#Инкапсуляция
import random


class BankAccount:
    def __init__(self, name, balance,password):
        #Открытые атрибуты public
        #_protected
        #__private
        self.name = name
        self._balance = balance
        self.__password = password
    def get_balance(self,password):
        if password == self.__password:
           return self._balance
        return 'невепный пароль'
    def get_money(self,password,amount):
        if password == self.__password:
            self._balance -= amount
            return self._balance
        return 'неверный пароль'

    def _random_password(self):
        return random.randint(1000000,99999999)


    def reset_password(self,old_password):
        if self.__password == self._random_password():
            new_password= self._random_password()
            self.__password = new_password
            return new_password
ardager=BankAccount('ardager',100, 'def232')
print(ardager.__password())




from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def voce(self):
        pass
class Dog(Animal):
    def move(self):
        return 'ходит'
    def voce(self):
        return 'гав гав'

my_dog = Dog()
print(my_dog.move())