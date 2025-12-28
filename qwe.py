import requests
from bs4 import BeautifulSoup
url = "https://rpgworldcomic.com/hot-nhat?type=all"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('h3', class_='title-news')

for i, t in enumerate(titles[:10], start=1):
    print(i,t.get_text(strip= True ))
    
# name = soup.find_all('h3', class_='')  
# view = soup.find_all('span', class_='')  

# for i in range(len(name)):
#     print(f"{i+1}.{name[i].get_text(strip=True)} - {view[i].get_text(strip=True)}")
    