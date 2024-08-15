import requests
from datetime import datetime
from get_stuff import get_stuff

TOKEN = get_stuff('pixela')
USER_NAME = "tamari-sauce"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

date = '20240815'
header = {

    "X-USER-TOKEN":TOKEN
}
body = {

    "quantity": "2000"
}

#Update a pixel
url = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
r = requests.put(url=url, json=body, headers=header)

print(r.text)

#Delete a pixel
r = requests.delete(url=url, headers=header)

print(r.text)
