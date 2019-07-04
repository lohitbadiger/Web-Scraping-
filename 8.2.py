from bs4 import BeautifulSoup as soup

# using the urllib Lib for this

from urllib.request import urlopen as uReq



#  This is Iphone scrapiing


my_url ="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient=uReq(my_url)

# open the urllib for the reading the file 'established 406'


page_html=uClient.read()


# connection  being stopped 
uClient.close()

# creating the soup container
# adding the Scraper 
# Html.parser


page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class": "_3O0U0u"})
# print(len(container))


# print(soup.prettify(container[0]))

container=containers[0]
print(container.div.img['alt'])




price=container.findAll("div",{"class": "col col-5-12 _2o7WAb"})

print(price[0].text)

rating=container.findAll("div",{"class": "hGSR34"})
print(rating[0].text)

filename="products_susumu.csv"
f=open(filename, "w")

headers="Products_Name, Pricing, Ratings\n"
print(f.write(headers))

for container in containers:
    product_name=container.div.img['alt']

    price_container=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container=container.findAll("div",{'class':"hGSR34"})
    rating=rating_container[0].text

    print("product_name: "+ product_name)
    print("price"+price)
    print("rating" + rating)


  
#   modifying the 

    # string parsing

    trim_price=''.join(price.split(','))
    rm_rupee=trim_price.split("₹")
    add_rs_price="Rs." + rm_rupee[1]

    split_price=add_rs_price.split("E")

    final_price=split_price[0]

    split_rating=rating.split(" ")
    final_rating=split_rating[0]

    print(product_name.replace(",", "|")+ " ," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + ","+ final_price + ", " +final_rating+"\n" )
f.close()


# Apple iPhone X (Space Gray, 64 GB)
# ₹69,999₹91,90023% offUp to ₹17,900 Off on ExchangeEMI starting from ₹2325/monthGet by 11 AM, TomorrowOffersNo Cost EMISpecial Price
# # 4.632

# Apple iPhone X (Space Gray, 64 GB)
# ₹69,999₹91,90023% offUp to ₹17,900 Off on ExchangeEMI starting from ₹2325/monthGet by 11 AM, TomorrowOffersNo Cost EMISpecial Price
# 4.632