from bs4 import BeautifulSoup

data_SL="""<ul class="content-col_discover">

        <h5>Discover</h5>
        <li><a href="/resources" id="free_resources"> Free Resources</a></li>
        <li><a href="http://community.simplilearn.com/" id="users"> Free Resources</a></li>
        
        <li><a href="career-data-labs" id="lab"> Career Data labs</a></li>

        <li><a href="/scholarships-for-veterans" id="scholarship">  
        Veterans scholarship</a></li>

        
        <li><a href="http://www.simplilearn.com/feed/" id="rss">RSS FEED</a></li>

            </ul>"""

# <!-- Create soup object -->

soup_SL=BeautifulSoup(data_SL, 'html.parser')

# if i do this i get all info
print(soup_SL)


# parse only part of the document, text values for  tags using getText method

print('___________________Get oly req___________')
print(soup_SL.get_text())

# import soupStrainer class for parsing th  e desired part of the web document

from bs4 import SoupStrainer

# create object to parse only the id (link) with lab
tags_with_LabLink=SoupStrainer(id="lab")

# print the part of the parsed document

print(BeautifulSoup(data_SL, 'html.parser', parse_only=tags_with_LabLink).prettify())

# without prettify function
# just arrenges the output neatly

print(' _______________________prettify function__________________ ')

print(BeautifulSoup(data_SL, 'html.parser', parse_only=tags_with_LabLink))








