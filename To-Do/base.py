from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    task = {'id': len(tasks) + 1, 'task': data['task'], 'completed': False}
    tasks.append(task)
    return jsonify(task)

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

@app.route('/toggle/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)

# index.html
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do App</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        .container { max-width: 500px; margin: auto; padding: 20px; }
        ul { list-style: none; padding: 0; }
        li { padding: 10px; display: flex; justify-content: space-between; }
        .completed { text-decoration: line-through; }
    </style>
</head>
<body>
    <div class="container">
        <h2>To-Do List</h2>
        <input type="text" id="taskInput" placeholder="Enter a task">
        <button onclick="addTask()">Add</button>
        <ul id="taskList"></ul>
    </div>
    <script>
        async function fetchTasks() {
            const response = await fetch('/tasks');
            const tasks = await response.json();
            document.getElementById('taskList').innerHTML = tasks.map(task => `
                <li class="${task.completed ? 'completed' : ''}">
                    ${task.task} 
                    <button onclick="toggleTask(${task.id})">✔</button>
                    <button onclick="deleteTask(${task.id})">✖</button>
                </li>
            `).join('');
        }
        async function addTask() {
            const task = document.getElementById('taskInput').value;
            if (task) {
                await fetch('/add', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({task})
                });
                document.getElementById('taskInput').value = '';
                fetchTasks();
            }
        }
        async function deleteTask(id) {
            await fetch(`/delete/${id}`, { method: 'DELETE' });
            fetchTasks();
        }
        async function toggleTask(id) {
            await fetch(`/toggle/${id}`, { method: 'PUT' });
            fetchTasks();
        }
        fetchTasks();
    </script>
</body>
</html>
"""
