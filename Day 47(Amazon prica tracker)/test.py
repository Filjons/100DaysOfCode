import requests
from bs4 import BeautifulSoup


URL = "https://appbrewery.github.io/"

user_input = "instant_pot"

responese = requests.get(url=f"{URL}{user_input}")

web_page = responese.text
soup = BeautifulSoup(web_page, "html.parser")
#print(soup.prettify())

# extract data (songs)
# CSS selectors to drill down in the tag tre
price_whole = soup.find(class_="a-price-whole").get_text()
price_fraction = soup.find(class_="a-price-fraction").get_text()
print(f"{price_whole}{price_fraction}")
# Save data to file
#file_name = f"web_search_{user_input}.txt"
#with open(file_name, "w", encoding="utf-8") as file:
#    file.write(soup.prettify())
