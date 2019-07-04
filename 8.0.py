# Trump Lies

# reading the web [page into Python


import requests
url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')


print(url.text[0:500])

print('____________________________________________________')

from bs4 import BeautifulSoup
soup=BeautifulSoup(url.text, 'html.parser')

print('____________________________________________________')

results=soup.findAll('span', attrs={'class':'short-desc'})
print(len(results))
print('____________________________________________________')

print(results[0:3])

print("____________________________________")

print("____________________________________")

# from the bottom of the website

print(results[-1])
print("____________________________________")
print("____________________________________")
print("____________________________________")

print("____________________________________")

# extracting the date

first_result=results[0]
print(first_result)


print("____________________________________")
print("_________________strong___________________")
print("____________________________________")

print("____________________________________")


print(first_result.find('strong'))
print("____________________________________")
print("____________________________________")



print(first_result.find('strong').text)

print("____________________________________")
print(first_result.find('strong').text[0:-5])


print("________________strong Data____________________")

# BELOW BOTH ARE SAME   
print(first_result.find('strong').text[0:-5]+ ', 2019')
print(first_result.find('strong').text , ', 2019')

print("__________________first_result__________________")

# extracting the Lie

# lets first see the results
print(first_result)

print("___________________contents_________________")
print(first_result.contents)
print("_________________contents[1])___________________")

# first results contents[1]
print(first_result.contents[1])
print("___________________contents_________________")

# we shall now remove the dot and quote from the text


print('_________________________________________________________________________')
print(first_result.contents[1][1:-2])


print('_________________________________________________________________________')

# extracting the explanations

print(first_result.contents[2])


print('_______________________________')

print(first_result.find('a'))

print('_______________________________')
print(first_result.find('a')['href'])


print('_______________________________')
print('_______________________________')


#3 Building the dataset

records=[]

for result in results:
    date=result.find('strong').text[0:-1]+', 2019'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie, explanation, url))

print(len(records))
print('_______________________________')

print(records[0:3])


print('_______________________________')




# import pandas as pd
# df=pd.DataFrame(records, columns=['date','lie','explanation','url'])




# print(df.head()) 

# print('_______________________________')


# print(df.tail())


# print('_______________________________')

# df['date']=pd.to_datetime(df['date'])
# print(df) 

# df.to_csv('susumu_trump.csv', index=False, encoding='utf-8')
# df=pd.read_csv('susumu_trump', parse_dates=['date'], encoding='utf-8')

