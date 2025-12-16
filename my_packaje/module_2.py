class Hero:
    def __init__(self, name, lvl,hp):
        #Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def base_method (self):
        return f"{self.name} {self.lvl} {self.hp}"