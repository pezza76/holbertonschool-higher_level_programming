from flask import Flask, jsonify, request

# Create a web app using the Flask toolkit
app = Flask(__name__)

tasks = []

# A GET route (like visiting a webpage)
@app.route('/')
def home():
    return "Welcome to the homepage!"

# new get route 
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# add a task with a post method
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    tasks.append(task)
    return jsonify(tasks), 201


detailed_tasks = []
@app.route('/tasks/detailed', methods=['POST'])
def add_detailed_task():
    data = request.get_json() 
    task = {
    "title": data['title'],
    "description": data['description'],
    "priority": data['priority']
}   
    detailed_tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/detailed', methods=['GET'])
def get_detailed_tasks():
    return jsonify(detailed_tasks), 200

extra_task = []
@app.route('/tasks/more', methods=['POST'])
def more_tasks():
    data = request.get_json() # Listen for a post request and convert the json to a python dict
    task = {'task': data['task']}
    extra_task.append(task)
    return jsonify(task), 201

@app.route('/tasks/more', methods=['GET'])
def view_more_tasks():
    return jsonify(extra_task), 200



# delete a task
@app.route('/delete/<int:index>')
def delete(index):
    if index >= 0 & index < len(tasks):
        removed = tasks.pop(index)
        return jsonify(removed)

if __name__ == '__main__':
    app.run(debug=True, port=5001)