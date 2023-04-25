from typing import Optional


# Задача 1. Создать родительский класс машина, у которого есть атрибуты model,
# age, color и weight, из них обязательный только model. Также у класса должны
# быть методы move, stop, birthday, методы move и stop выводят сообщение на
# экран "move" , "stop" , а birthday увеличивает атрибут age на 1.
# Если атрибут age = None, то выбрасывает исключение с сообщением "атрибут age не задан".

class Car:
    def __init__(self, model, age=None,color=None,weight=None):
        self.model=model
        self.age=age
        self.color=color
        self.weight=weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def get_birthday(self):
        try:
            return 1 + self.age
        except Exception:
            print("атрибут age не задан")

car_1=Car("BMW","White")
car_1.move()
car_1.stop()
car_1.get_birthday()


# Задача 2. Есть csv файл со списком людей, нужно прочитать его и преобразовать
# в список датаклассов. То есть нужно создать датакласс с атрибутами name, age,
# при этом тип age : Optional[int]. У датакласса должно быть property birth_year,
# которое считает возраст

import csv

person_= [['name', 'age'],
         ['lena', '24'],
         ['dima'],
         ['vova','35']]

with open('person_new.csv','w+') as f:
    writer=csv.writer(f)
    for row in person_:
        writer.writerow(row)


with open('person_new.csv') as f:
    print(f.read())

from typing import Optional

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: Optional[int]
    age=None

    @property
    def birth_year(self):
        return 2023 - self.age

person_1=Person(name ='lena', age=24)
person_2=Person(name ='dima')
person_3=Person(name ='vova', age=35)
print(person_1.birth_year)
print(person_2.name)



