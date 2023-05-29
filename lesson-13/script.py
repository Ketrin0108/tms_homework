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
        self.todo_id = todo_id
        self.user_id = user_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"Todo: {self.todo_id}, User: {self.user_id}, Title: {self.title}, Completed: {self.completed}"


class Todos:
    def __init__(self):
        self.todos = []
        for todo in requests.get(URL).json():
            self.todos.append(Todo(todo['id'], todo['userId'], todo['title'], todo['completed']))
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

    def to_dict(self):
        return [todo.__dict__ for todo in self.todos]

    def from_dict(self, todos_data):
        self.todos = []
        for todo_data in todos_data:
            todo = Todo(
                todo_data['todo_id'],
                todo_data['user_id'],
                todo_data['title'],
                todo_data['completed']
            )
            self.todos.append(todo)

    def save_json(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.to_dict(), f)

    def load_json(self, file_name):
        with open(file_name, 'r') as f:
            todos_data = json.load(f)
            self.from_dict(todos_data)


todos = Todos() # создаем экземпляр класса



print(len(todos))  # Выводит количество задач

todo_id = 10 # получаем todo по id
todo = todos.get_todo_by_id (todo_id)
print(f"Todo with id {todo_id}: {todo}")


for todo in todos:
    print(todo)  # иттерация повсем todo



todos.save_json('todo.json') # сериализуем список todo в файл todo.json

todos.load_json('todo.json') # загружаем список todo из файла todo.json


# выводим список todo после загрузки из файла
for todo in todos:
    print(todo)





