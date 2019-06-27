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

print('________________________________')
variable=soup.h1
print(variable)

print('________________________________')
variable2=soup.p
print(variable2)

print('________________________________')
variable3=soup.b.comment

print(variable3)