class Product:
    def __init__(self,title,price,quantity):
        self.title=title
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f'Название продукта:{self.title},цуна {self.price} количество{self.quantity}'
    def __repr__(self):
        return f'Product(title={self.title!r}, price={self.price!r}, quantity={self.quantity!r})'

    def __eq__(self, other):
        if self.title == other.title:
            return True
        return False

    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False

    def __add__(self, other):

        return Product("Combo", self.price + other.price, 1)
product1=Product('Ноут',1000, 2)
product2=Product('Ноут',500,3)
product3=Product('Айфон',600,5)
print(product1==product2)
print(product3<product2)
conbo=product1+product3
print(conbo)