import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/search/?filter=topsellers"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract game titles
titles = soup.find_all('span', class_='title')

# Print the top 10 best-selling games
for i, title in enumerate(titles[:10], start=1):
    print(f"{i}. {title.get_text(strip=True)}")