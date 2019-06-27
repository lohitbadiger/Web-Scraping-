# 11.5

# Demo3 Naviagting tree

# import the required lib

from bs4 import BeautifulSoup

# create the document
book_shop_doc= """
<catalog>

<head> <title>The web book catalog</title></head>
<p class="title"> <b>The Book Catalog</b></p>
<books>
    <book id="bk001">
        <Author> HighTower</Author>
    <genre>Fiction</genre>
<price>44.34</price>
<pub_date>2000-10-10</pub_date>
<review>An Amazing story of nothing.</review>

    </book>
    <book id="bk002">
        <author>Nagata, Suanne</author>
        <title>Becoming somebody</title>
        <genre>Biography </genre>
        <review>A masterPiece of the art</review>

    </book>

    <book id="bk003">
        <author> Oberg, Bruce </author>
        <title>The Poet's First Poem</title>
        <genre>Poem</genre>
        <price>28.2</price>
        <review>The Least Poetic Poems</review>

    </book>
</books>
</catalog>

"""

# create a soup objects


book_soup=BeautifulSoup(book_shop_doc, 'html.parser')
# print the catalog tag
 
print(book_soup)

print("-____"*50)
#  create a sup objects
print(book_soup.catalog)


print("-____"*50)

# get head

print(book_soup.head)
print("-____"*50)
# get title tag

title_tag=book_soup.title
print(title_tag)
print("-____"*50)

# print catalog bold tag
# navigate down the descendants and print dem

print('________++++++++++++++++++++++++++++++___________-')
for descen in book_soup.head.descendants:
    print(descen)
print('________===========================___________-')

# navigate down using stripped string method
for string in book_soup.stripped_strings:
    print(repr(string))

print('________==========parent=================___________-')

# navigate up using the parent method
print(title_tag.parent)


print('________============navigate back and forth===============___________-')

# create element object to navigate back and forth
element_soup=book_soup.catalog.books
print(element_soup)

print('________===========================___________-')


next_element=element_soup.next_element.next_element
print(next_element)


print('________===========================___________-')

# navigate back using the previous_element method
previous_element=next_element.previous_element.previous_element
print(previous_element)

print('________===========================___________-')

# create a sibling object and navigator to view it

next_sibling = book_soup.catalog.books.book
print(next_sibling)


# navigator to next sibling
next_sibling2=next_sibling.next_sibling
print(next_sibling2.next_sibling)

# navigate to previous sibling
previous_sibling=next_sibling2.previous_sibling
print(previous_sibling)