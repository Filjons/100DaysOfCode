from flask import Flask
app = Flask(__name__)


@app.route('/')
def front_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://www.bing.com/images/search?q=100+mL+Flask&FORM=IRIBIP" alt="">'


if __name__ == '__main__':
   app.run()
