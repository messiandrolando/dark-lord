import requests
import pandas as pd
search_term = "iphone 17"
url = f"https://www.amazon.in/s?k={search_term.replace(' ', '+')}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(f"HTTP Status Code: {response.status_code}")
tables = pd.read_html(response.text)
for i, table in enumerate(tables):
    print(f"Bảng {i}:")
    print(table)

