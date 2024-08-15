
import json


SECRET_FILE = 'secret_stuff.json'

last_key = None
last_stuff = None

def get_stuff(key=''):

    global last_key, last_stuff
    stuff = last_stuff

    if key != last_key:

        with open(SECRET_FILE) as secret_file:
            file = json.load(secret_file)
            stuff = file[key]

        last_key = key
        last_stuff = stuff
        return stuff

    else:
        return stuff