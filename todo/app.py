from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

tasks = []
users = {}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == ['POST']:
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists'
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))
    data = request.json
    task = {'id': len(tasks) + 1, 'task': data['task'], 'completed': False}
    tasks.append(task)
    return jsonify(task)

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

@app.route('/toggle/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks', methods=['GET'])
def get_tasks():
    if 'username' not in session:
        return redirect(url_for('login'))
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
