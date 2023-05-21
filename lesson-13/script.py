# Сделать get запрос на https://jsonplaceholder.typicode.com/todos и
# преобразовать данные в инстанс класса Todos, который будет содержать в себе
# список todo - где каждый элемент является экземпляром класса Todo.
# Реализовать для класса Todos поведение контейнера: сделать его итерируемым,
# добавить возможность получения todo по id, а также добавить возможность
# сериализации и десериализации (запись и чтение из json)

import requests
from dotenv import load_dotenv
import json

load_dotenv()
URL = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(URL)
todos_json = response.json()
print(response.json())


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



todos = Todos()

todos.from_json(todos_json)

#with open(todo_file.json, "w+") as write_file:
    #json.dump(data, write_file)

#with open("todo_file.json") as read_file:
    #a = json.load(read_file)

# НЕ ЗНАЮ КАК ДАЛЬШЕ , НЕ ПОНИМАЮ


