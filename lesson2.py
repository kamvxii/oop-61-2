#Родительский класс
class Hero:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def action(self):
        return f'{self.name} {self.score}'
Naruto = Hero('Naruto', 100)
#дочерний класс
class Maze(Hero):
    def cast_spell(self):
        return f'{self.name} {self.score}'
    def ___init__(self, name, score,mp):
        super().__init__(name, score)
        self.mp = mp
    def action(self):
        return f'{self.name} {self.score}'
Sasuke=Maze('Sasuke', 100, )#Необязательно писать еще раз
print(Sasuke.action())
print(Naruto.action())
print(Sasuke.cast_spell())