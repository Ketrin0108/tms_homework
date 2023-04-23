# Задание 1.
# Дописать функцию так, чтобы она возвращала None в случае если ключа
# нет, а не генерировала исключение (для реализации используем исключения)
# def func(dict_,key):
      #return dict_[key]

dict_={
    "name":"Kira",
    "age":25
}
key="sex"

def func(dict_,key):
    try:
        return dict_[key]
    except KeyError:
        return None

print(func(dict_,key))




# Задание 2.
# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

a="зима"
b="весна"
c="лето"
d="осень"

with open("weather.txt","w+", encoding='utf-8') as write_file:
    write_file.write(str(a + "\n" + b + "\n"))

with open("weather.txt","a",encoding='utf-8') as write_file:
    write_file.write(str(c + "\n" + d ))


# Задание 3. Создать словарь в качестве  ключа будет 6-ти значное число (id),
# а в качестве значений кортеж сосотящий из 2-ух элементов - имя(str), возраст (int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.

import json

data={
    123456:
        (('Kate',25),('Kira',20), ('Artem', 36), ('Lena', 22),('Inna', 40), ('Yulia', 29))
}
print(json.dumps(data))

with open("data_file.json", "w+") as write_file:
    json.dump(data, write_file)

# Задание 4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон".
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)


import csv

data=[['name', 'age', 'телефон'],
      ['Kate','25'],
      ['Kira','20'],
      ['Artem', '36'],
      ['Lena', '22'],
      ['Inna', '40'],
      ['Yulia', '29']]

with open('data_file_new.csv', 'w+',encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('data_file_new.csv',encoding='utf-8') as f:
    print(f.read())

with open('data_file_new.csv',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    list_=[]
    for row in reader:
        print(row)
        list_.append(row)









