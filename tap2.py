from bs4 import BeautifulSoup

html = """
<html>
  <head><title>trang beta cua toi</title></head>
  <body>
    <h1>Xin chào!</h1>
    <p class="mota">Đây là đoạn văn đầu tiên cua toi.</p>
    <p id="gioithieu">Đây là đoạn văn thứ hai cua toi.</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

print(soup.title.string)            
print(soup.h1.string)               
print(soup.find('p', class_='mota').string)       
print(soup.find('p', id='gioithieu').string)      