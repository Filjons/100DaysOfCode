from flask import Flask
app = Flask(__name__)


#set FLASK_APP=hello.py

#from flask import Flask
#app = Flask(__name__)


#@app.route('/')
#def hello_world():
#   return 'Hello World’

#if __name__ == '__main__':
#   app.run()

#app.run(host='127.0.0.1',port=8000,debug=True)


# For windows systems to environmental variables
# export FLASK_APP=app.py # your python file name
# set FLASK_APP = app.py
# export FLASK_ENV=development
# set FLASK_DEBUG = True
# python -m flask --app hello run

# More info: https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
   app.run()
