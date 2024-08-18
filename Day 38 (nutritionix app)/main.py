import requests
from get_stuff import get_stuff


USER_NAME = "tamari-sauce"
PROJ_NAME = "My_workout"
SHEET_NAME = "1SMyId07U-dL07fk6x3rKoU84wwb8bugK7t6MA-r8PgA"
SHEETY_EP = f"https://api.sheety.co/{USERNAME}/{PROJ_NAME}/{SHEET_NAME}"

NUTRI_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"


def nutri_post(query=""):
    credentials = get_stuff('nutritionix')
    header = {
        "Content-Type": "application/json",
        "x-app-id": credentials['id'],
        "x-app-key": credentials['token']
    }
    body = {"query": f"{query}"}

    return(requests.post(url=NUTRI_EP, json=body, headers=header))

def sheety_add_row(query={}):
    credentials = get_stuff('sheety')
    header = {
        
        "Authorization": f"Bearer {credentials['token']}"
    }
    body = {"query": f"{query}"}

    return(requests.post(url=SHEETY_EP, json=body, headers=header))

def sheety_get_row(row=int):
    credentials = get_stuff('sheety')
    header = {
        "Authorization": f"Bearer {credentials['token']}"
    }
    row_url = f"{SHEETY_EP}/{row}"

    return(requests.get(url=row_url, headers=header))

if __name__ == "__main__":
    q = {
        "date":"20/20/2020",
        "time":"20:20",
        "exercise":"walking",
        "duration":"32",
        "calories":"135"
          }
    r = sheety_add_row(query=q)
    
    r = nutri_post()
    print(r['token'])

