from bs4 import BeautifulSoup
import requests

# define url for simplilearn 

url='https://simplilearn.com/'

# access result through requests objcts
result=requests.get(url)

#load the page content
page_content=result.content

# create soup object
soup=BeautifulSoup(page_content, 'html.parser')



# view the contents
print(soup.contents)

print('-__________________________')

print(soup.prettify())

#view the original encoding
print('-__________________________')

print(soup.original_encoding)



print('-__________________________')
# format the tag a to xml
print(soup.body.a.prettify(formatter='xml'))

print('-__________________________')


# define a custom function to convert string value to uppercase

def upperCaseFn(strt):


    return strt.upper()



print('-__________________________')

# format using custom function for outputting string texts in uppercase

print(soup.body.a.prettify(formatter=upperCaseFn))

