
# import the Bs4
from bs4 import BeautifulSoup


# import the web sccraping example htmlxfile as per your locations


HTMLFILEPATH="D:\machine_Learning\programming with py 3.x\web scraping\web2.html"
with open(HTMLFILEPATH,"r") as organization:
    soup=BeautifulSoup(organization, "html.parser") 

# view the contents from the soup
print(soup.contents)
print('____________________________________')


# search the content of the soup object

tag_li=soup.find("li")

# chck  object type
print(type(tag_li))
print('_______________print object_____________________')

print(tag_li)

print('________________start searching in the treee by find method____________________')


#select the 'HR' id
find_id=soup.find(id="HR")
# print the associated 


print(find_id)
print('____________________________________')

# print the string value


print(find_id.li.div.string)


print('_________________***___________________')


# search for  the perticular css attr
search_for_stringOnly=soup.find(text=['LOHIT', "KOTA"])
print(search_for_stringOnly)

print('____________________________________')


search_for_stringOnly=soup.findAll(text=['LOHIT', "KOTA"])
print(search_for_stringOnly)



 

print('____________________________________')





# to get the 'class' of 'ITmanager'

css_class_search=soup.find(attrs={"class":"ITmanager"})



print(css_class_search)

print('____________________________________')
print('____________________________________')
print('________________is_account_manager____________________')


# create a function to search the document  based on the name


def is_account_manager(tag):
    return tag.has_attr("id") and tag.get("id")=="Finance"


# 

# Im using find method to get id and id='finance'
is_account_manager=soup.find(is_account_manager)

# view the account manager string name

print(is_account_manager.li.div.string)

print('____________________________________')

print('____________________________________')
print('____________________________________')

# this will give you all the tag with there string names

for tag in soup.findAll(True):
    print(tag.name)
print('_______________________________________________________________')
print('_________________________HRManager______________________________________')

# this step to get class of HRManager
# this is present as list

find_class=soup.findAll(class_="HRManager")
print(type(find_class))

print('____________________________________')
#
# Now im printing the HRmanager Tag index of 0.

print(find_class[0])

print('____________________________________')
print('_______________________________________________________________')


# this will give the index 1
print(find_class[1])

print('____________________________________')

 
print('____________________________________')

# lets store find_class zero index in find_class variable

find_class=find_class[0]

find_parent=find_class.find_parents("ul")



print(find_parent)

print('____________________________________')

 
print('______________finddddddddddddddALLLL______________________')

do_it=soup.findAll(class_='HR')

find1=do_it[0]
find_para=find1.find_parents('div')
print(find_para)
print('____________________________________')

print('____________________________________')

# this will give the id="IT"

org=soup.find(id="IT")
print(org)
print('____________________________________')
print('____________________________________')
print('____________________________________')
print('____________________________________')


# below 


next_sibling=org.findNextSiblings()
print(next_sibling)

print('____________________________________')
print('____________________________________')
print('________________Again im printing the parent____________________')


parent=org.find_parent

# print parents
print(parent)
print('____________________________________')

print('____________________________________')
print('_____________previous_______________________')



# search all previous tags

all_previous=org.findAllPrevious()
print(all_previous)
print('____________________________________')




previous_sibling=org.findPreviousSibling()

print(previous_sibling)
print('________________findAllNext____________________')

all_next=org.findAllNext()


print(all_next)
print('____________________________________')


# run this in jupyter

from bs4 import BeautifulSoup
import re


email_example=""" <br>
<p>My Email Is</p>
abc@efskjf@gmail.com"""
soup_email=BeautifulSoup(email_example, "lxml")
email_ID_regexp=re.compile("\w+@\w+\.\w+")
email_id=soup_email.find(text=email_ID_regexp)
print(email_id)