from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>This is my 1st flask heroko app using github.</h1>'