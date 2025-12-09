class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health

    def info(self) -> str:
        return f'{self.name}, {self.age} лет, здоровье {self.health}'

    def use_ability(self) -> str:
        return f'{self.name} использует базовую способность.'


class Flyable:
    def use_ability(self) -> str:
        return super().use_ability()+'летает.'

class Swimmable:
    def use_ability(self) -> str:
        return super().use_ability()+'плавает.'

class Invisible:
    def use_ability(self) -> str:
        return super().use_ability()+'становится невидимым.'
class Climbing:
    def use_ability(self) -> str:
        return super().use_ability()+'карабкается по стенам'

class Duck(Animal,Flyable,Swimmable):
    pass
duck = Duck("Дональд", 3, 80)

class Bat(Animal,Flyable,Invisible):
    pass
bat = Bat("Бэтти", 5, 60)

class Frog(Animal,Swimmable,Climbing):
    pass
frog = Frog("Фроппи", 2, 50)

class Phoenix(Animal,Flyable,Invisible):
    def reborn(self):
        self.health = 200
        return f"{self.name} возрождается из пепла с полным здоровьем!"
phoenix = Phoenix("Феникс", 100, 200)
class Zoo:
    class Zoo:
        def __init__(self):
            self.animals: list[Animal] = []

        def add_animal(self, animal: Animal):
            self.animals.append(animal)

        def show_all(self):
            for animal in self.animals:
                print(animal.info())

        def perform_show(self):
            for animal in self.animals:
                print(animal.use_ability())