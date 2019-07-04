from bs4 import BeautifulSoup

this_is_html="""
<ul class="jambotron mt-5">


    <div>
            <h5>This is new Round of Tag</h5>


    </div>

            <li>
                    <a href="lohitbadiger.heroku" id="lohit">This is my personal website</a>

            </li>
            
            <li>
            <a href="googele.heroku" id="google">This is my search engine</a>
            
            </li>
           
            <li>
                    <a href="match_me.heroku" id="match">This is match me site</a>
                    
            </li>

            <li>
                    <a href="okgoing.heroku" id="ok">This is ok and going</a>

                    
            </li>


    
</ul>"""
# <!-- Create soup object -->

soup_take=BeautifulSoup(this_is_html,'html.parser')

# if i want to scrape only the small portions of the data 
print("'''''''''''''''''''''''''''''''")


print('soup_take.get_text(): ', soup_take.get_text())

print("__________________soupstainer_____________________")

# Now import soupstainer class


from bs4 import SoupStrainer

give_only=SoupStrainer(id="google")
print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only))

print("_______________________________________")


give_only=SoupStrainer(id="lohit")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only))

print("_______________________________________")

give_only=SoupStrainer(id="match")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only))

print("_______________________________________")


give_only=SoupStrainer(id="ok")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only))


print("________________--------____________________")

print("________________--------____________________")



give_only=SoupStrainer(id="google")
print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only).prettify())
print("_______________________________________")


give_only=SoupStrainer(id="lohit")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only).prettify())

print("_______________________________________")

give_only=SoupStrainer(id="match")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only).prettify())

print("_______________________________________")


give_only=SoupStrainer(id="ok")

print(BeautifulSoup(this_is_html, 'html.parser', parse_only=give_only).prettify())





