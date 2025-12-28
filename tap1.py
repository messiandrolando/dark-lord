import requests
from bs4 import BeautifulSoup

# Bước 1: Gửi request đến website
url = "https://store.steampowered.com/search/?filter=topsellers"
response = requests.get(url)

# Bước 2: Phân tích HTML
soup = BeautifulSoup(response.text, "html.parser")

# Bước 3: Tìm tất cả các quote
quotes = soup.find_all('span', class_='text')

for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")