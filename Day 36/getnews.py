
from datetime import date
import json
from textwrap import indent
import requests


API_KEY = '3d2a22d2d96b47e39f879636c766ee64'
DATE = date.today()
url = (
    f'https://newsapi.org/v2/top-headlines?q=Tesla&from={DATE}&pageSize=3&apiKey={API_KEY}')

r = requests.get(url)

with open('news_file.json' ,'w') as file:
    # Writing data to a file
    file.write(json.dumps(r.json(), indent=4))
    

'''
for title in r.json():
    print(r.json()['articles'])
#head_lines = r.json()['articles']
#print(head_lines)'''