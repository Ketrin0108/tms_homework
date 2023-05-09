# 1. Напишите генератор, который будет генерировать числа от 0 до бесконечности
# и вызовите его несколько раз

import random

def get_num_generator():
    i = 0
    while True:
        i += 1
        yield i

generator = get_num_generator()
print(next(generator))  # выведет 1
print(next(generator))  # выведет 2
print(next(generator))  # выведет 3
print(next(generator))  # выведет 4

# 2.Напишите итератор, который будет генерировать числа от 0 до заданного
# (по сути реализовать функцию range только в виде итератора)

class Range_Iterator:

    def __init__(self, stop):
        self.stop = stop
        self.counter = 0 # создаем отдельный атрибут

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.stop:
            number = self.counter
            self.counter += 1
            return number
        raise StopIteration # если не создадим ошибку будет бесконечный цикл None

my_range=Range_Iterator(20)

for i in my_range:
    print(i)


# 3. Допишите класс Family таким образом чтобы он влялся итератором
# и мы могли при помощи цикла for вывести всех ченов семьи

class Family:

     def __init__(self, last_name, members):
         self.last_name = last_name
         self.members = members
         self.index = 0

     def __len__(self):
         return len(self.members)

     def __iter__(self):   # реализовываю итератор
         return self

     def __next__(self):   # реализовываю итератор
         if self.index < len(self.members):
             result = self.members[self.index]
             self.index += 1
             return result
         raise StopIteration

     def add_family_member(self, member):
        self.members.append(member)

     def __str__(self):
         return f"Family: last_name - {self.last_name}, count - {len(self.members)}"

class FamilyMember:

    def __init__(self, name, role=None, age=None):
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember: {self.name}, role: {self.role}"


son = FamilyMember(name="Roma", role="son")
father = FamilyMember(name="Nikita", role="father", age=43)
mather = FamilyMember(name="Lena", role="mather", age=40)

members = [son, father, mather]

family = Family(last_name="Гаврильчик", members=members)

for i in members:
    print(i)


# Допишите классы таким образом чтобы у FamilyMember был id
# и в классе Family мы могли найти member по id


class Family:

     def __init__(self, last_name, members):
         self.last_name = last_name
         self.members = members
         self.index = 0

     def __len__(self):
         return len(self.members)

     def __iter__(self):   # реализовываю итератор
         return self

     def __next__(self):   # реализовываю итератор
         if self.index < len(self.members):
             result = self.members[self.index]
             self.index += 1
             return result
         raise StopIteration

     def add_family_member(self, member):
        self.members.append(member)

     def find(self, id):
         return next((member for member in self.members if member.id == id), None)


     def __str__(self):
         return f"Family: last_name - {self.last_name}, count - {len(self.members)}"



class FamilyMember:

    def __init__(self,id, name, role=None, age=None):
        self.id = id
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember: id: {self.id}, name: {self.name}, role: {self.role}"


son = FamilyMember(id= 1, name="Roma", role="son")
father = FamilyMember(id= 2, name="Nikita", role="father", age=43)
mather = FamilyMember(id= 3, name="Lena", role="mather", age=40)

members = [son, father, mather]

family_1 = Family(last_name="Гаврильчик", members=members)

print(family_1.find(id=2))
#  5.Реализовать генератор чисел Фибоначчи

def fibonacci():
    x,y= 0,1
    while True:
        yield x
        x,y = y,x +y

fib = fibonacci()

for i in range(10):
    print(next(fib))

# 5. Реализовать у Family возможность взятия элемента по индексу - family[0] - при помощи метода getitem


class Family:

    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
        self.index = 0

    def __len__(self):
        return len(self.members)

    def __iter__(self):  # реализовываю итератор
        return self

    def __next__(self):  # реализовываю итератор
        if self.index < len(self.members):
            result = self.members[self.index]
            self.index += 1
            return result
        raise StopIteration

    def __getitem__(self, item): # вызываю метод магический метод getitem
        return self.members[item]


    def add_family_member(self, member):
        self.members.append(member)

    def find(self, id):
        return next((member for member in self.members if member.id == id), None)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"


class FamilyMember:

    def __init__(self, id, name, role=None, age=None):
        self.id = id
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember: id: {self.id}, name: {self.name}, role: {self.role}"


son = FamilyMember(id=1, name="Roma", role="son")
father = FamilyMember(id=2, name="Nikita", role="father", age=43)
mather = FamilyMember(id=3, name="Lena", role="mather", age=40)

members = [son, father, mather]

family_1 = Family(last_name="Гаврильчик", members=members)

for member in family_1:
    print(member)

print(family_1[1])

