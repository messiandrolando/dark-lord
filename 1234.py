import pandas as pd
from bs4 import BeautifulSoup 
import requests

url = 'https://vnexpress.net/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(response.status_code)

title = soup.find_all('h3', class_='title-news')
data = []

for i, t in enumerate(title[:10], 1):
    titles = t.get_text(strip=True)
    link = t.find('a')
    link = link['href'] if link else 'Không có link'
    data.append((i, titles, link))

df = pd.DataFrame(data, columns=['STT', 'Tiêu đề', 'Liên kết'])
print(df)

df.to_excel('tintuc.xlsx', index=False, engine='openpyxl')
print("Thành công")