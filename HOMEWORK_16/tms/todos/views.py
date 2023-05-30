from django.http import JsonResponse
from django.shortcuts import render
import requests
import json

# Create your views here

RESPONSE = requests.get("https://jsonplaceholder.typicode.com/todos").json()


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
        for todo in requests.get(TODOS_URL).json():
            self.todos.append(Todo(todo['id'], todo['userId'], todo['title'], todo['completed']))
        self.current = 0

    def __len__(self):
        return len(self.todos)

    def __iter__(self):  # иттератор
        return iter(self.todos)

    def __next__(self):
        if self.current < len(self.todos):
            todo = self.todos[self.current]
            self.current += 1
            return todo
        else:
            raise StopIteration

    def get_todo_by_id(self, todo_id):  # возможность на todo по id
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


def home(request):
    todos = Todos()
    todos.from_dict()
    return render(request, 'home.html', {'todos': Todos})


def todo(request):
    return JsonResponse({'todos.to_json': RESPONSE})


# Create your views here.
from django.shortcuts import render

# Create your views here.
