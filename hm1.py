class Singers:
    def __init__(self,name,age,hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.hungry=True

    def round_song(self):
        return f'{self.name} поет Clematis'
    def eat(self,pizza='еда'):
        self.hungry = False
        "Мизи просит еды :3"

        return f'{self.name} съел {pizza} и теперь не умрет'
    def round_score(self):
        return f'{self.name} получил скор 87/86'
    def base_method(self):
        return f'{self.name} {self.age} {self.hair_color}'
Mizi = Singers("Mizi", 12,'pink' )
Sua=Singers("Sua", 54, "Black")

print(Mizi.eat())
print(Mizi.round_score())

print(Sua.eat())