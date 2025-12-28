import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/" 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

bang = soup.find('table', id='main_table_countries_today')  
dong = bang.tbody.find_all('tr')  


with open('covid_data.csv', 'w', newline='', encoding='utf-8') as f:
    ghi = csv.writer(f)
    ghi.writerow(['Tên quốc gia', 'Tổng số ca nhiễm', 'Số ca tử vong', 'Số ca hồi phục']) 

    for d in dong[:20]: 
        cot = d.find_all('td')
        tenquocgia = cot[1].get_text(strip=True)
        tongso_ca = cot[2].get_text(strip=True)
        so_tuvong = cot[4].get_text(strip=True)
        so_hoiphuc = cot[6].get_text(strip=True)  
        ghi.writerow([tenquocgia, tongso_ca, so_tuvong, so_hoiphuc])

print("Dữ liệu đã lưu vào file covid_data.csv thành công!")