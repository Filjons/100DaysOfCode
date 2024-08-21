import requests
from get_stuff import get_stuff


USER_NAME = "tamari-sauce"
PROJ_NAME = "myWorkouts"
SHEET_NAME = "workouts"
SHEETY_EP = f"https://api.sheety.co/{USER_NAME}/{PROJ_NAME}/{SHEET_NAME}"


def sheety_get_row(row=2):
    credentials = get_stuff('sheety')
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['token']}"
    }
    row_url = f"{SHEETY_EP}/{row}"

    return (requests.get(url=row_url, headers=header))


if __name__ == "__main__":

    r = sheety_get_row()
    print(r.json())
    print(r.text)
