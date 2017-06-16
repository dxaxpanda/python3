from flask import Flask,request


server = Flask(__name__)

@server.route('/hello')
def hello():
    return "Hello World !"

@server.route('/user')
def get_user():
    name = request.args.get('name')

    return "Requested for name = {}".format(name)

@server.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    return f"Login successful for {username}, {password}. "

@server.route('/save', methods=['POST'])
def save_user():
    user_data = request.json

    return "Saving user with id = {}.".format(user_data.get('id'))

server.run(port=8000)
