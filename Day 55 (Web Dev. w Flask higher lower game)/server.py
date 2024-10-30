from flask import Flask
from random import randint
app = Flask(__name__)


def make_bold(function):
    def wrapper(*args):
        result = f"<b>{function(*args)}</b>"
        return result
    return wrapper


def make_italic(function):
    def wrapper(*args):
        result = f"<em>{function(*args)}</em>"
        return result
    return wrapper


def make_underline(function):
    def wrapper(*args):
        result = f"<u>{function(*args)}</u>"
        return result
    return wrapper


@app.route('/')

def front_page():
    return '<h1>This is Flask!</h1>' \
        '<img src="https://eduscienceuk.com/wp-content/uploads/2018/09/ES-Flask-Conical-NM-LR-.jpg" width=200 alt="">'


@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"


@app.route('/<int:num>')

def number(num):
    random_num = randint(0, 9)

    if num > random_num:
        return '<h1 style="color: red">Too high!</h1><br><br>' \
               '<img src="https://media3.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif" width=300>'
    elif num < random_num:
        return '<h1 style="color: blue">Too low!</h1><br><br>' \
               '<img src="https://media3.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif" width=300>'
    elif num == random_num:
        return '<h1 style="color: green">Correct!</h1><br><br>' \
               '<img src="https://media3.giphy.com/media/de7siRDyeOBpe/giphy.gif">'
    
if __name__ == '__main__':
    app.run()
