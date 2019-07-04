from bs4 import BeautifulSoup as bs 


html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <p class="new">Lohit</p>
    <h1 class="new">Lohit</h1>

    <h2>London</h2>
        <h2>Mumba</h2>
        



<b><!-- "new comment "--> </b>
</body>
</html>"""


soup=bs(html_doc, 'html.parser')

print(soup)

print('_____________variable___________________')
variable=soup.h1
print(variable)

print('_______________variable2_________________')
variable2=soup.p
print(variable2)

print('______________variable3__________________')
variable3=soup.b.string

print(type(variable3))
