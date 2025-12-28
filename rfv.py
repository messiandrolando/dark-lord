from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/" 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

bang = soup.find('table', id='main_table_countries_today')  
dong = bang.tbody.find_all('tr')  
wb = Workbook()
ws = wb.active
ws.title="COVID-19 Data"
ws.append(["Tên quốc gia', 'Tổng số ca nhiễm', 'Số ca tử vong', 'Số ca hồi phục"])

for d in dong[:20]: 
    cot = d.find_all('td')
    tenquocgia = cot[1].get_text(strip=True)
    tongso_camac = cot[2].get_text(strip=True)
    so_tuvong = cot[4].get_text(strip=True)
    so_hoiphuc =  cot[6].get_text(strip=True) 
    ws.append ([tenquocgia, tongso_camac, so_tuvong, so_hoiphuc])

wb.save("covid_data2.xlsx")