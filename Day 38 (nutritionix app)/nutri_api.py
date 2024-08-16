import requests
from get_stuff import get_stuff

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

def get_cred():
    return(get_stuff('nutritionix'))

def nutri_post():
credentials 

app_id = credentials['id']
app_key = credentials['token']

header = {
    "Content-Type": "application/json",
    "x-app-id": app_id,
    "x-app-key": app_key
}
body = {"query": "swam for 1 hour"}

r = requests.post(url=ENDPOINT, json=body, headers=header)


if __name__ == "__main__":

    r = get_stuff("nutritionix")
    print(r['token'])