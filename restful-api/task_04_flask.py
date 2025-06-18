from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}

@app.route("/data")
def get_users():
    ls = []
    for i in users:
        ls.append(i)
    return jsonify(ls)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user_obj(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    users[username] = {
    "name": name,
    "age": age,
    "city": city
    }

    return jsonify({"message": "User added successfully", "user": users[username]})



if __name__ == "__main__":
    app.run(debug=True)
