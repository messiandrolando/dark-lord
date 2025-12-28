import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"  
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

quocgia = soup.find_all('div', class_='col-md-4 country')  

for i, quocgias in enumerate(quocgia[:10], 1):
    tenquocgia = quocgias.find('h3').get_text(strip=True)
    danso = quocgias.find('span', class_='country-population').get_text(strip=True)
    dientich = quocgias.find('span', class_='country-area').get_text(strip=True)
    print(f"{i}. {tenquocgia}")
    print(f"Dân số: {danso}")
    print(f"Diện tích: {dientich}")