class Hero:
    #конструктор класса
    def __init__(self, name, lvl,hp):
        #Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def base_method (self):
        return f"{self.name} {self.lvl} {self.hp}"
        #Объект экземпляр
Naruto=Hero("Naruto",50,50)
print(Naruto.name)
Sasuke=Hero("Sasuke",50,50)
print(Sasuke.name)