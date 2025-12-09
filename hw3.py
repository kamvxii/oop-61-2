class Product:
    def __init__(self,name,price):
        self.name = name
        self._price= price
        self.__discount=0
    def get_price(self):
        price_after_discount = self._price - self.__discount/100
        return price_after_discount
    def set_price(self,percent):
        if percent > 0:
            percent=0
        if percent >50:
            percent=50
        self.__discount=percent
    def apply_secret_discount(self,secret_code):
        if secret_code=='VIP123':
            self.percent =+5
        return 'неверный скидочный код'


p=Product("Iphone", 1000)

p.set_discount(20)
print("Цена со скидкой:", p.get_price())

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())


from abc import ABC, abstractmethod
class PaymentMethod(Product):
    @abstractmethod
    def pay(self,amount):
        pass
    def refund(self,amount):
        pass

class CardPayment(PaymentMethod):
     def pay(self, amount):
        print(f"Оплата картой: {amount}")

     def refund(self, amount):
        print(f"Возврат на карту: {amount}")

class CashPayment(PaymentMethod):
     def pay(self, amount):
            print(f"Оплата наличными: {amount}")

     def refund(self, amount):
            print(f"Возврат наличными: {amount}")

class CryptoPayment(PaymentMethod):
     def pay(self, amount):
            print({
                "type": "crypto",
                "amount": 'amount',
                "currency": "USDT"
            })

     def refund(self, amount):
            print({
                "type": "crypto_refund",
                "amount": 'amount',
                "currency": "USDT"
            })
class PaymentProcessor:
    def __init__(self,payment_method):
        self.payment_method = payment_method
    def process(self, amount):
        self.payment_method.pay(amount)
