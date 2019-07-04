from bs4 import BeautifulSoup

# create th e
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
soup = BeautifulSoup(html_doc, 'html.parser')

print('__________type of soup_____')
print(type(soup))

print('__________printing the soup_____')

print(soup)


print('_________________tag_________________')
tag=soup.p
print(tag)

comment=soup.b.string
print(type(comment))
print('_________print comment__________')
print(comment)

print('_________print comment by slicing__________')
print(comment[0:])

print('_________print comment by slicing__________')
print(comment[0:10])

print('_________print comment by slicing__________')
print(comment[0:6:2])

print('______________________________')

print(tag.string)

print('______________________________')
print(comment.string[0:7:])

print('______________________________')
print(tag.attrs)
print('______________________________')
print(tag.string)


print('_____________________________*******************************************____________________________________________________')

from bs4 import BeautifulSoup
# create a html document

html_doc="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <h1> This is heading</h1>
   

            <p title="This is about me" class="test">
                        my first website web scrape
            </p>
    
    
            <div class="cities">
            
                    <h2>London</h2>
                    <h2>Mumba</h2>
                    
            </div>

                 <b> ""This is 'comment' l""</b>
</body>
</html>"""


# parse it using the html parser
soup=BeautifulSoup(html_doc, 'html.parser')

# view the soup type
print(type(soup))

print('_____________ view the soup object_______________________')
# view the soup object
print(soup)

print('___________________***********************_______________')
print(soup.p)

print('___________________***********************_______________')
# create tag obkec
tag=soup.p

print(tag)
print('___________________***********************_______________')

# create a comment object type
comment=soup.b.string
print(comment)
print(type(comment))
print('___________________***********************_______________') 

# print tag attributes
print(tag.attrs)
print('___________________***********************_______________')

# print tag string
print(tag.string)
# print the navigable string

print(type(tag.string))