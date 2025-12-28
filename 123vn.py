import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_qu%E1%BB%91c_gia_theo_d%C3%A2n_s%E1%BB%91_n%C4%83m_2012'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

print(response.status_code)

# Try to use lxml if available, otherwise fall back to the built-in parser
try:
	soup = BeautifulSoup(response.text, "lxml")
except Exception as e:
	# bs4 raises FeatureNotFound specifically when parser is missing, but
	# catching Exception is safer if import/parsing issues differ across envs
	print("Warning: 'lxml' parser not available or failed. Falling back to 'html.parser'. To remove this warning, install lxml: pip install lxml")
	soup = BeautifulSoup(response.text, "html.parser")

table = soup.find('table', class_='wikitable')

if table is None:
	print("No table with class 'wikitable' found on the page.")
else:
	df = pd.read_html(str(table))[0]
	print(df)