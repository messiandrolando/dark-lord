from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
table=soup.find("table",{"class":"wikitable"})

rows=table.find_all("tr")
data=[]
for row in rows:
    cols= row.find_all(["th","td"])
    cols=[c.text.strip() for c in cols]
    print(cols)
    data.append(cols)

df=pd.DataFrame(data)
df.to_excel('pokemon.xlsx',index=False)    