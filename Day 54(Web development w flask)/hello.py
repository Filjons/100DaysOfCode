from flask import Flask
app = Flask(__name__)

#For windows systems to environmental variables
#set FLASK_APP=hello.py
#
@app.route('/')
def hello_world():
    return 'hello world!'