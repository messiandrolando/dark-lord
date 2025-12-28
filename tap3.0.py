from bs4 import BeautifulSoup

html = '''
<div class="item">
  <h2 class="product-name">Chuột máy tính</h2>
  <span class="price">200,000 VND</span>
</div>
<div class="item">
  <h2 class="product-name">Bàn phím cơ</h2>
  <span class="price">800,000 VND</span>
</div>  # đoạn HTML ở trên
'''
soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('div', class_='item')

for item in items:
    name = item.find('h2', class_='product-name').text
    price = item.find('span', class_='price').text
    print(f"Sản phẩm: {name} - Giá: {price}")