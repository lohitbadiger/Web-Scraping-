from bs4 import BeautifulSoup as Bs

snap_deal_scrape='https://www.snapdeal.com/products/books-academic-professional?sort=plrty'

soup=Bs(snap_deal_scrape,"html.parser")

print('____Soup________')
print(type(soup))


books=soup.contents

print(books)

