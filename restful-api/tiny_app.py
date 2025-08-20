from flask import Flask, render_template, request
from flask_restx import Api, Resource
import mysql.connector

app = Flask(__name__)
api = Api(app)

# connect app to a mysql database
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'users_db2'
)

@api.route('/')
class Home(Resource):
    def get(self):
        return {"Welcome": "Welcome to the homepage"}

if __name__ == '__main__':
    app.run(debug=True)