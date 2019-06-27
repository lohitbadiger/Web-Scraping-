# import bs4 fro  BeautifulSoup
from bs4 import BeautifulSoup

# create the doc
html_doc="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<h1> Heading</h1>
    <b> ""This is 'comment' l""</b>

    <p title="This is about me" class="test">my first website web scrape</p>
    <div class="cities">
    
    <h2>London</h2>
    <h2>Mumba</h2>
    
    </div>
    
</body>
</html>"""
# parse it using html parser

soup = BeautifulSoup(html_doc, 'html.parser')

# view the soup type

print('__________type of soup_____')
print(type(soup))

#view the soup object
print('__________printing the soup_____')

print(soup)

# create a tag obejc
print('_________________tag_________________')
tag=soup.p

# print the tag
print(tag)
print('_______________________________')

# below line will give only string inside <b>tag
comment1=soup.b.string


# below line will give only <b> tag
comment=soup.b


print(type(comment))

# print the comment 
print('_________print comment__________')
print(comment)


print('_______________________________')
print('_______________________________')







print('_______________print the comment by slicing_______________')

print(comment1[0:])

print('_______________print the comment by slicing_______________')

print(comment1[0:4])

print('_________print comment by slicing__________')
print(comment1[0:10])


# contains indices (1, 3)
print(comment1[0:6:2])

# if 

print('______________________________')

print(tag.string)


print('______________________________')
print(comment.string[0:7:])