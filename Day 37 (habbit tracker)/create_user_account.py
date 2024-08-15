import requests
from datetime import datetime
from get_stuff import get_stuff

TOKEN = get_stuff('pixela')
USER_NAME = "tamari-sauce"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username":USER_NAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

#response = requests.post(url=pixela_endpoint, json=parameters)
#print(response.text)


graph_config = {
    "id":GRAPH_ID,
    "name":"Coding",
    "unit":"minutes",
    "type":"int",
    "color":"kuro"
}

header = {
    "X-USER-TOKEN":TOKEN
    }

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

#response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
#print(response.text)

new_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

d = datetime.now()
date = d.strftime('%Y%m%d')

poster = {
    "date": date,
    "quantity": "120",
}

r = requests.post(url=new_graph_endpoint, json=poster, headers=header)
#Bad solution
while r.json()['isSuccess'] == False:
    r = requests.post(url=new_graph_endpoint, json=poster, headers=header)

