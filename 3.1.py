from bs4 import BeautifulSoup

htmlfile="D:/machine_Learning/programming with py 3.x/web scraping/web3.html"

with open(htmlfile,"r") as orgz:
    soup=BeautifulSoup(orgz,"html.parser")


print(soup.contents)
print("-----------"*4) 


tag_lr=soup.find("table")

print(type(tag_lr))

print("-----------"*4) 

print(tag_lr)
print("---------%--"*4) 

find_name=soup.find(id="name")
print(find_name)

print('-------------------printing Lohit------------------------------------')
print(find_name.tr.td.string)

print('~ %'*20)
print(find_name.find(attrs={"class":"lo"}))

print('-------------------printing classs------------------------------------')

search_perticular_string=soup.findAll(text=["whitefield", 'Banglore'])
print(search_perticular_string)

print('------------------- classs------------------------------------')

# css class attribute now

css_class_attrs=soup.find(attrs={'class':"location"})
print(css_class_attrs)


# next_sibling