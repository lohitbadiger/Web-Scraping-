# import the reqiuired lib
print('__________________________________________________________')
from bs4 import BeautifulSoup

from urllib.request import urlopen

url='https://simplilearn.com/resources'

webpage=urlopen(url)

sl_soup=BeautifulSoup(webpage,'html.parser')

webpage.close()


print(sl_soup.contents)

print(sl_soup.prettify())


print('_____________________title___________________________________________')
print(sl_soup.title)

print('______________________________href__________________________________')
for href in sl_soup.findAll("a", href=True):
    print(href["href"]) 


print('______________________findAll_____h2_____________________________________')

for article in sl_soup.findAll("h2"):
    print(article.string)

print('_____________________________.findAll("h4")___________________________________')



for article_topic in sl_soup.findAll("h4"):
    print(article_topic.string)


print('____________________________url2url2url2url2______________________________')



url2="https://www.simplilearn.com/what-is-tensorflow-article?source=frs_home"

webpage2=urlopen(url2)

sl_article=BeautifulSoup(webpage2,"html.parser")

test=sl_article.find(class_="desig_author empty-text")

type(test)

print(test.findAll("p"))

print('_______________________________________________________________________')

first_next_p=test.p

print(first_next_p)
print('_______________________________________________________________________')

find_next_sibling=first_next_p.next_sibling.next_sibling
print(find_next_sibling)

print('_______________________________________________________________________')



print(find_next_sibling.previous_sibling.previous_sibling)