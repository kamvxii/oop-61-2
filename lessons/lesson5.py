class Math:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract( j, i):
        return j-i
print(Math.add(1,2))
print(Math.subtract(1,2))
#Можно вызвать через класс
#Неизависит от обьекта
#Для утилитных функций

#Метод класса classmethod
class User:
    #Атрибуты класса
    default_role='guest'
    def __init__(self,name,role:str ='n/a'):
        #Атрибуты экземпляра класса
        self.name=name
        self.role=role
    @classmethod
    def create_from_name(cls,name):
        return cls(name,cls.default_role)
    @classmethod
    def create_from_role(cls,role):
        return cls(role,cls.default_role)



class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self.__price=value
iphone= Product("iphone 17 pro max",1000)
print(iphone.price)
print()





def simple_decorator(func):
    def wrapper(*args,**kw):
        print('до выполнения')
        func()
        print('после выполнения')
    return wrapper
@simple_decorator
def greeting():
    print('hello world')
greeting()

def greeting_decorator(func):
    def wrapper(name):
        print(f' hello{name}')
        func(name)
    return wrapper
def greeting_name(name):
    print(f'hyd {name}')
greeting_name('kamila')






def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator
@repeat_decorator(8)
def say_hello(name):
    print(f'hello {name} ')
say_hello('kama')



def class_decorator(cls):
   class NewClass(cls):
       def new_method(self):
           return 'im new method'
   return NewClass
@class_decorator
class OldClass:
    def old_method(self):
        return 'im old method'
obj1=OldClass()
print(obj1.new_method())



def check_subscribe(func):
    def wrapper(user,comm):
        if user.subscribe in ['test','test2']:
            func(user,comm)
        else:
            print('вы не подписаны на каналы')
    return wrapper
def is_admin_decorator(func):
    pass