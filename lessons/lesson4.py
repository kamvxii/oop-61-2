#dunder methods
class Test:
    def __init__(self,name='sasuke'):
        self.name = name
    def __str__(self):
        return self.name
my_dog = Test()
print(my_dog.name)
my_str = [1,2,3]
print(my_str)
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #+
    def __add__(v1,v2):
        print(v1.x+v2.x)
v1 = Vector(23,22)
v2 = Vector(3,4)
print(v1 + v2)
class Mylist:
    def __init__(self,value):
        self.value = value
    def __setitem__(self,key,value):
        print(key)
        print(value)
my_list=Mylist([1,2,3])
my_list[0]=3


class Mylist:
    def __init__(self):
        self.count = 0
    def __call__(self,*args,**kwargs):
        self.count =+1
my_list=Mylist()
print(my_list.count)
