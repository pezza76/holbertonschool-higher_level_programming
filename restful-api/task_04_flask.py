from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

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

if __name__ == "__main__":
    app.run(debug=True)
