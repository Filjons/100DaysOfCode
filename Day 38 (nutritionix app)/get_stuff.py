
import json

SECRET_FILE = 'secret_stuff.json'

last_key = None
last_stuff = None

def get_stuff(key=''):

    global last_key, last_stuff
    stuff = last_stuff

    if key != last_key:

        with open(SECRET_FILE) as secret_file:
            f = json.load(secret_file)
            stuff = f[key]

        last_key = key
        last_stuff = stuff
        return stuff

    else:
        return stuff


if __name__ == "__main__":

    r = get_stuff("sheety")
    print(r['token'])
