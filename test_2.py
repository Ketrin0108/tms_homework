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


#







