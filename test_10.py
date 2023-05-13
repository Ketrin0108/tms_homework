
# Техническое задание:
# Есть магазин, продукт (товар), покупатель, корзина и список покупок - это все отдельные классы,
# атрибуты и методы которых нужно продумать самостоятельно для того чтобы реализовать логику ниже

# Часть 1. Спроектировать классы.
# Написать классы:

# Продукт - атрибуты: id, name, price, amount
# Магазин - список продуктов (объектов класса Product)
# Покупатель - id, количество денег, список продуктов (названия: молоко, сыр и тд),
# которые нужно купить - все задается при инициализации покупателя
# Корзина - id, список продуктов (объектов класса Product - по умолчанию None)

# Часть 2. Написать бизнес-логику
# Реализовать следующие возможности:

# Создается покупатель с определенным количеством денег и списком продуктов
# Покупатель приходит в магазин и берет корзину (покупателю при помощи метода создается и добавляется корзина)
# Создать экземпляр магазина, который должен быть синглтоном, в котором будет список продуктов
# Покупатель проходится по списку продуктов, которые ему нужно купить и смотрит,
# есть ли в магазине эти продукты, если продукт есть, то покупатель добавляет его
# в свою корзину (нужен метод для добавления продукта Product в корзину)
# ТОЛЬКО ПРИ УСЛОВИИ что у покупателя достаточно денег. В ином случае вывести сообщение.
# Если денег достаточно, то покупатель добавляет продукт в корзину и количество этого продукта
# в магазине уменьшается на 1
# После того как прошлись по всем продуктам, вывести сообщение о том,
# какие продукты были куплены, а какие не были

from abc import ABC, abstractmethod

class Product:

    def __init__(self,id=None,name=None,price=0,amount=0):
        self.id=id
        self.name=name
        self.price=price
        self.amount=amount


    @abstractmethod
    def add_cost(self):
        pass

    @classmethod
    def new_product(cls,id,name,price,amount):
        return cls(id,name,price,amount)


class Shop:

    def __new__(cls, *args): # new управляет созданием нового экземпляра класса
        if not hasattr(cls, 'shop'):
            cls.shop = super(Shop, cls).__new__(cls)
        return cls.shop

    def __init__(self, products=None):
        self.products=products or []


class Basket:
    def __init__(self):
        self.list_=[]

    def add_basket(self,product):
        self.list_.append(product)

class Buyer:

    def __init__(self,id,money,list_product,basket=None):
        self.id=id
        self.money=money
        self.list_product=list_product
        if basket is None:
            self.basket = Basket()
        else:
            self.basket = basket

    def add_basket(self):  # смотрит есть ли продукт в магазине и добовляет в новую корзину
        for buyer_product in self.list_product:
            for product in Shop().products:
                if buyer_product.name == product.name:
                    if self.money >= product.price:
                        self.basket.add_basket(buyer_product)
                        self.money -= product.price
                        product.amount -= 1
                        break
                    else:
                        print(f"{self.id} не хватает денег на {product.name}")
            else:
                print(f"{self.id} продукта {buyer_product.name} нет в магазине")



products = [
    Product(id=1, name='Молоко', price=2, amount=5),
    Product(id=2, name='Сыр', price=5, amount=10),
    Product(id=3, name='Хлеб', price=1, amount=10),
    Product(id=4, name='Рыба', price=10, amount=4),
    Product(id=5, name='Мясо', price=15, amount=6),
    Product(id=6, name='Творог', price=6, amount=10),
    Product(id=7, name='Банан', price=4, amount=10),
    Product(id=8, name='Мука', price=3, amount=5)
]

shop=Shop(products)
print(Shop().products)

buyer = Buyer(id='user1', money=50, list_product=[Product.new_product(6, 'Творог', 6, 1), Product.new_product(7, 'Банан', 4, 1)])
buyer.add_basket()
print(buyer.basket.list_)
