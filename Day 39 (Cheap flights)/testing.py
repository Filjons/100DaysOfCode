import requests
import os
from get_stuff import get_stuff


USER_NAME = "c3cacb5163317a3fc90abc43cfd73795"
PROJ_NAME = "myWorkouts"
SHEET_NAME = "workouts"
SHEETY_EP = f"https://api.sheety.co/{USER_NAME}/{PROJ_NAME}/{SHEET_NAME}"


def sheety_get_row(row=1):
    credentials = get_stuff('sheety')
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['token']}"
    }
    row_url = f"{SHEETY_EP}/{row}"

    return (requests.get(url=row_url, headers=header))


if __name__ == "__main__":

    '''r = sheety_get_row(2)
    print(r.json())
    print(r.text)'''
    vars = os.environ.values
    print(f"{vars} \n")
    ENV_VAR = os.environ[
       "PATH"]
    print(type(ENV_VAR))
    print(ENV_VAR)
    var_list = ENV_VAR.split(";")
    ind = ENV_VAR.find("\\Microsoft\\WindowsApps")
    print(ind)
    print(var_list)
    print(ENV_VAR[450:460])
