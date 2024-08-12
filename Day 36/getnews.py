
from datetime import date
import json
import requests
from get_stuff import get_stuff

API_KEY = get_stuff('newsapi_key')
#DATE = date.today()
#print(DATE)
DATE = '2024-08-10'
url = (f'https://newsapi.org/v2/everything?q=tesla&language=en&from={DATE}&apiKey={API_KEY}')

r = requests.get(url)

with open('news_file.json' ,'w') as file:
    # Writing data to a file
    file.write(json.dumps(r.json(), indent=4))
    

'''
for title in r.json():
    print(r.json()['articles'])
#head_lines = r.json()['articles']
#print(head_lines)'''