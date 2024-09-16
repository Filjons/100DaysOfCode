from bs4 import BeautifulSoup
import requests

# get all data from the web page
url = "https://news.ycombinator.com/news"
responese = requests.get(url)

web_page = responese.text
# parse the data into a soup using the html.parser
soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())
article_tag = soup.find(name="span", class_="titleline",)
# print(article_tag)
article_text = article_tag.get_text()
article_link = soup.find(name="a")["href"]
article_upvote = soup.find(name="span", class_="score").get_text()

print(article_text, article_link, article_upvote)
'''for tag in story_list:
    print(tag.text)'''


'''
with open("Day 45\\bs4-start\\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#how to get all tags?
all_tags = soup.find_all(name="a")

for tag in all_tags:
    print(tag.text)

section_heading = soup.find_all(name="h3", class_="heading")
for tag in section_heading:
    print(tag.text)


company_url = soup.select_one(selector="p")

print(company_url)'''
