import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

# Write your code below this line 👇
#user_input = input("Which year do you want to travel to? (YYY-MM-DD): ")
user_input = "1988-03-19"
responese = requests.get(url=f"{URL}/{user_input}")

web_page = responese.text
# parse the data into a soup using the html.parser
soup = BeautifulSoup(web_page, "html.parser")
#print(soup.prettify())
#CSS selectors to drill down in the tag tree
ranked_list = soup.select(selector="div ul li #title-of-a-story")
print(ranked_list)
file_name = f"top_100_songs_{user_input}.txt"

with open(file_name,"w", encoding="utf-8") as file:
    [file.write(f"{song.get_text()}\n") for song in ranked_list]
'''
with open(file_name, "r") as file:
    print(file.read())'''