 # Функции

 # Задание 1: Даны списки:
 #
 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 #
 # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 #
 # Нужно вернуть список, который состоит из элементов, общих для этих двух списков

a = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def func(a,b):
    list_ = [i for i in a if i in b]
    print(f"result= {list_}")
    return (a, b)

func(a, b)

#  Объявить функцию, которая принимает в себя любое количество словарей и возвращает единый словарь,
#  в котором есть ключи из всех переданных словарей

def func(*args):
    dict_1={}
    for dict_ in args:
        for key in dict_:
            dict_1[key]=dict_[key]
    return(dict_1)
a={
    "name": "kira",
    "sex": "women"
}
b={
    "age": 25
}
print(func(a,b))

# Декораторы

# Написать декоратор, который возвращает int вместо float (хотим получить 1 вместо 1.5 как в примере)

#def div(a, b):
    #return a / b
#div(3, 2)

def wrapper(func):
    def div(a,b):
        print(int(a/b))
    return div
@wrapper
def print_chisla():
    return a/b
print_chisla(3,2)

# Написать декоратор, который будет просить пользователя ввести число до тех пор,
# пока он не введет положительное число

def wrapper(positive_int):
    def inner():
        while True:
            result = positive_int()
            if result > 0:
                return result
    return inner

@wrapper
def input_positive_int():
    return int(input("Введите положительное число"))

input_positive_int()







