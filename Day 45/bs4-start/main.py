from bs4 import BeautifulSoup

with open("Day 45\\bs4-start\\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
'''
#how to get all tags?
all_tags = soup.find_all(name="a")

for tag in all_tags:
    print(tag.text)

section_heading = soup.find_all(name="h3", class_="heading")
for tag in section_heading:
    print(tag.text)

'''
company_url = soup.select_one(selector="p")

print(company_url)