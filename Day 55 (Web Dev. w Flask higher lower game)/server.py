from flask import Flask
app = Flask(__name__)

@app.route('/')
def front_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://eduscienceuk.com/wp-content/uploads/2018/09/ES-Flask-Conical-NM-LR-.jpg" ialt=""/>'


if __name__ == '__main__':
   app.run()
