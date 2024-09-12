from bs4 import BeautifulSoup

with open("Day 45\\bs4-start\\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#how to get all tags?
print(soup.find_all(name="a"))