from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def data():
    return jsonify(list(users.values()))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {"username": username}
    return jsonify(users[username]), 201

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
