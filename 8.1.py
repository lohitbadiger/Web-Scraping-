import requests
url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

from bs4 import BeautifulSoup
soup=BeautifulSoup(url.text,'html.parser')

results=soup.find_all('span', attrs={'class':'short-desc'})

records=[]

for result in results:
    date=result.find('strong').text[0:-1]+', 2019'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie, explanation, url))

import pandas as pd
df=pd.DataFrame(records, columns=['date','lie','explanation','url'])

df['date']=pd.to_datetime(df['date'])
print(df) 

df.to_csv('susumu_trump.csv', index=False, encoding='utf-8')
df=pd.read_csv('susumu_trump.csv', parse_dates=['date'], encoding='utf-8')

