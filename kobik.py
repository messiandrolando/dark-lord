import requests
from bs4 import BeautifulSoup
url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_qu%E1%BB%91c_gia_theo_d%C3%A2n_s%E1%BB%91"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")
for r in rows:
    cols = r.find_all(["th", "td"])
    cols = [c.text.strip() for c in cols]  
    print(cols)