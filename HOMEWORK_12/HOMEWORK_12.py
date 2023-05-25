# Написать класс-коллекцию (итератор) Zoo, в котором будет название зоопарка и
# список животных (Animal с property - имя, тип (енот, тигр и тд),  возраст).
# У класса Zoo должны быть реализованы следующие методы:
# - append (добавить животное)
# - get (получить животное по id)
# - get_by_type (получить животное по типу)
# - delete - удалить животное из списка по id
#
# По zoo мы должны уметь итерироваться и брать элемент по индексу,
# а также получать длину len(zoo) и уметь красиво выводить объект при
# приведении к строке (например, Зоопарк: имя зоопарка, n животных)
#
# В классе Animal должны быть как минимум два classmethod, которые умеют создавать
# животное определенного типа с возрастом 0 и принимают в себя только имя, например:
# - create_tiger(cls, name)

# Дополнительно: написать class-decorator, который логгирует время работы функций класса
# в файл с именем функции и временем вызова
class Zoo:
    def __init__(self, name, animals):
        self.name = name
        self.animals= animals
        self.index = 0

    def __len__(self):
        return len(self.animals)

    def __iter__(self): #иттератор
        return self

    def __next__(self):
        if self.index < len(self.animals):
            result = self.animals[self.index]
            self.index += 1
            return result
        raise StopIteration


    def add_zoo_animal(self, animal): #метод append добавить животное
        self.animals.append(animal)

    def __getitem__(self, item): # вызываю метод магический метод getitem
        return self.animals[item]


    def get_by_id(self, id):
        for animal in self.animals:
            if animal.id == id:
                return animal
        return None

    def delete_by_id(self, animal_id): # метод удалить животное по id
        for animal in self.animals:
            if animal.id == animal_id:
                self.animals.remove(animal)
                break
        else:
            print(f"Животное с id {animal_id} не найдено в зоопарке")

    def __str__(self):
        return f"Зоопарк:  {self.name} имеет {len(self.animals)} животных"

class Animal:
    def __init__(self, id, name, animal_type, age=0):
        self.id = id
        self.name = name
        self.animal_type = animal_type
        self.age = age

    @classmethod
    def create_mammal(cls, id, name):
        return cls(id, name, "Млекопитающее", 0)

    @classmethod
    def create_bird(cls, id, name):
        return cls(id, name, "Птица", 0)

class Bird(Animal):
    def __init__(self,id, name, animal_type, age):
        super().__init__(id, name, animal_type, age)

class Mammal(Animal):
    def __init__(self,id, name, animal_type, age):
        super().__init__(id, name, animal_type, age)

elephant = Animal.create_mammal(1,'Мальта')
print(elephant.name)
print(elephant.animal_type)
print(elephant.age)

mammal1 = Mammal(id=1, name='тигр', animal_type='Млекопитающие', age=10)
mammal2= Mammal(id=2, name='рысь', animal_type='Млекопитающие', age=15)
mammal3 = Mammal(id=3, name='лев', animal_type='Млекопитающие', age=5)
bird1 = Bird(id=4, name='орел', animal_type='Птица', age=5)
bird2 = Bird(id=5, name='ара', animal_type='Птица', age=7)

zoo = Zoo('Центральный',[])

zoo.add_zoo_animal(mammal1)
zoo.add_zoo_animal(mammal2)
zoo.add_zoo_animal(mammal3)
zoo.add_zoo_animal(bird1)
zoo.add_zoo_animal(bird2)
print(len(zoo)) #проверяю количество животных в зоопарке
print(zoo[0].name)
print(zoo[1].name)

for animal in zoo: #проверяю доступ к элементам зоопарка через итератор
    print(animal.name)

print(zoo.get_by_id(1).name) #нахожу животное по id

zoo.delete_by_id(3) #удаляю животное по id
zoo.delete_by_id(2)

print(len(zoo)) #проверяю количество животных в зоопарке после удадения

print(zoo)

