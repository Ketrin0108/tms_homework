# Сделать get запрос на https://jsonplaceholder.typicode.com/todos и
# преобразовать данные в инстанс класса Todos, который будет содержать в себе
# список todo - где каждый элемент является экземпляром класса Todo.
# Реализовать для класса Todos поведение контейнера: сделать его итерируемым,
# добавить возможность получения todo по id, а также добавить возможность
# сериализации и десериализации (запись и чтение из json)

from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

URL= os.environ.get("URL")



class Todo:
    def __init__(self, todo_id, user_id, title, completed):
        seld.todo_id = todo_id
        self.user_id = user_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"Todo: {self.todo_id}, User: {self.user_id}, Title: {self.title}, Completed: {self.completed}"


class Todos:
    def __init__(self):
        self.todos = []
        for todo in requests.get(URL).json():
            self.todos.append(Todo(todo_id = todo['id'], title = todo['title'],completed = todo['completed']))
        self.current = 0

    def __len__(self):
        return len(self.todos)

    def __iter__(self): # иттератор
        return iter(self.todos)

    def __next__(self):
        if self.current < len(self.todos):
            todo = self.todos[self.current]
            self.current += 1
            return todo
        else:
            raise StopIteration

    def get_todo_by_id (self, todo_id): # возможность на todo по id
        for todo in self.todos:
            if todo.todo_id == todo_id:
                return todo
        return None

    def from_json(self, json_data):
        todos_data = json.loads(json_data)
        for todo_data in todos_data:
            todo = Todo(
                todo_data['id'],
                todo_data['userId'],
                todo_data['title'],
                todo_data['completed']
            )
            self.todos.append(todo)

    def serialis(self):
        with open(todo_file.json, "w+") as write_file:
            json.dump(self.todos, write_file)

    def desirialis(self):
        with open("todo_file.json") as read_file:
            self.todos = json.load(read_file)
        return self.todos


todos = Todos() # создаем экземпляр класса

todos.from_json(todos_json) # заполняем список todo в классе Todos

print(len(todos))  # Выводит количество задач

for todo in todos:
    print(todo)  # иттерация повсем todo

todo_id = 1
todo = todos.get_todo_by_id(todo_id) # получить todo по id

if todo:
    print(f"Todo with id {todo_id}: {todo}")
else:
    print(f"Todo with id {todo_id} not found")




