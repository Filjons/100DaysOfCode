import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

responese = requests.get(url=URL)

web_page = responese.text
# parse the data into a soup using the html.parser
soup = BeautifulSoup(web_page, "html.parser")
#print(soup.prettify())
ranked_list = soup.find_all(name="h3", class_="title",)

with open("top_100_movies.txt","w", encoding="utf-8") as file:
    [file.write(f"{movie.get_text()}\n") for movie in ranked_list[::-1]]

with open("top_100_movies.txt", "r") as file:
    print(file.read())