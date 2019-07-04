
# import the lib

from bs4 import BeautifulSoup
import requests

# url for web scraping

url='https://lohitbadiger.herokuapp.com/'


# acccess the url for web scraping
result=requests.get(url)

# scraoe the webpage content

webpage=result.content
sl_soup=BeautifulSoup(webpage,'html.parser')

result.close()


print("''''''''''''''''''''--------contents------------''''''''''''''''''''")
# create a soup object to parse the webpage using html parser


#View the content of the soup object
print(sl_soup.contents)

print("''''''''''''''''''''---------prettify-----------''''''''''''''''''''")

#use the prettify() method to view a well formatted output (with html tags)

print(sl_soup.prettify())


print("''''''''''''''''''''-----head--------------''''''''''''''''''''")
#View the head of the soup object

print(sl_soup.head)

print("''''''''''''''''''''------title--------------''''''''''''''''''''")


#View the title of the webpage

print(sl_soup.title)
print("''''''''''''''''''''---------findAll-----------''''''''''''''''''''")

#Find all the links present in the webpage

for href in sl_soup.findAll('a', href=True):
    print(href('href'))