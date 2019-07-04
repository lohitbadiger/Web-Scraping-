from bs4 import BeautifulSoup as bs


html="3.html"
with open(html, "r") as read:
    soup=bs(read, "html.parser")


print(soup.contents)