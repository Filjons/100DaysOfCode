
from datetime import date
import json
import requests
from secret_stuff import API_KEY_NEWSAPI

API_KEY = API_KEY_NEWSAPI

DATE = date.today()
url = (f'https://newsapi.org/v2/everything?q=tesla&from={DATE}&apiKey={API_KEY}')

r = requests.get(url)

with open('news_file.json' ,'w') as file:
    # Writing data to a file
    file.write(json.dumps(r.json(), indent=4))
    

'''
for title in r.json():
    print(r.json()['articles'])
#head_lines = r.json()['articles']
#print(head_lines)'''