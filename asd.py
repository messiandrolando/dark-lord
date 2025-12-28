import requests
from bs4 import BeautifulSoup

url = "https://rpgworldcomic.com/hot-nhat?type=all"
headers = {'User-Agent': 'Mozilla/5.0'}  
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('h3', class_='series-title')
views = soup.find_all('span', class_='view-count')

for i in range(min(len(titles), len(views))):
    title = titles[i].get_text(strip=True)
    view = views[i].get_text(strip=True)
    print(f"{i+1}. {title} - {view}")headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('h3', class_='series-title')
views = soup.find_all('span', class_='view-count')

for i in range(min(len(titles), len(views))):
    title = titles[i].get_text(strip=True)
    view = views[i].get_text(strip=True)
    print(f"{i+1}. {title} - {view}")

