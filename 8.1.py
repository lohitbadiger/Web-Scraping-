
# import functions 
import requests

# url from New York Times On trump Lies

url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')


# importing the BS Library


from bs4 import BeautifulSoup
soup=BeautifulSoup(url.text,'html.parser')

# class short-desc is stored in the results

#  check for the alterations in this

results=soup.find_all('span', attrs={'class':'short-desc'})


# empty records list initally

records=[]

for result in results:
    date=result.find('strong').text[0:-1]+', 2019'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie, explanation, url))

# using the pandas as data framework for easy listing
import pandas as pd

# df  creating the columns as data....

df=pd.DataFrame(records, columns=['date','lie','explanation','url'])

# creating the date in different format

df['date']=pd.to_datetime(df['date'])
print(df) 

# making the csv file for the Trump Lies

df.to_csv('susumu_trump.csv', index=False, encoding='utf-8')
df=pd.read_csv('susumu_trump.csv', parse_dates=['date'], encoding='utf-8')

