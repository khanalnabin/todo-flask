import time
import pickle

from flask import Flask, render_template, redirect, url_for,  request

app = Flask(__name__)

todos = []
try:
    with open('todos.pickle', 'rb') as f:
        todos = pickle.load(f)
except FileNotFoundError:
    print("Not Found")


@app.route('/')
def index():
    return render_template('todo.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    if len(todo) > 0:
        id = int(time.time()*1000)
        todos.append({'id': id, 'todo': todo})

        with open('todos.pickle', 'wb') as f:
            pickle.dump(todos, f, protocol=pickle.HIGHEST_PROTOCOL)
    return redirect(url_for('index'))


@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    for i in range(len(todos)):
        if todos[i]['id'] == id:
            todos.pop(i)
            with open('todos.pickle', 'wb') as f:
                pickle.dump(todos, f, protocol=pickle.HIGHEST_PROTOCOL)
            break
    return redirect(url_for('index'))


@app.route('/<id>/update', methods=['GET', 'POST'])
def update(id):
    return redirect(url_for('index'))
