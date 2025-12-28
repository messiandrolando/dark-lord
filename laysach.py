from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<h1>Welcome to my Page</h1>
<p class="intro">Xin chào, tôi tên là ko co ten</p>
<p class="intro">Quốc tịch: <img
src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Fl
ag_of_Vietnam.svg/1280px-Flag_of_Vietnam.svg.png" width="40"></p>
<p id="content">Đây là trang giới thiệu về môn học lập trình
của tôi</p>
<p class="footer">Liên hệ cho tôi qua duong day ma tuy :))</p>
<ul>
<li><img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="20">Python</li>
<li><img src="https://cdn-icons-png.flaticon.com/512/226/226777.png" width="20">Java</li>
<li><img src="https://cdn-icons-png.flaticon.com/512/6132/6132222.png" width="20">C++</li>
<li><img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png" width="20">JavaScript</li>
</ul>
<div><p>Hello</p><p>World</p><p>Beautiful</p><span>Soup</span><p>is</p><b>Great!</b></div>
<h2>Danh sách các bạn chung lớp của tôi</h2>
<ul>
<li>Trần Uy</li>
<li>Tô Hoàng Lập</li>
<li>Tô Gia Phúc</li>
<li>Nguyễn Minh Quân</li>
<li>Trần Phú Cường</li>
</ul>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

print("=== 1. find() ===")
print("Thẻ <p> đầu tiên:", soup.p.get_text())
print("Thẻ <p id='content'>:", soup.find(id="content").get_text(), "\n")

print("=== 2. find_all() ===")
langs = [li.get_text() for li in soup.find_all("li")]
print("Danh sách ngôn ngữ:", *["- "+x for x in langs], sep="\n")
print("\n2 phần tử đầu tiên:", *["- "+x for x in langs[:2]], sep="\n", end="\n\n")

print("=== 3. prettify() ===")
print(soup.prettify(), "\n")

print("=== 4. replace_with() ===")
soup.find("p", class_="footer").string.replace_with("Liên hệ quản trị viên")
print("Footer sau khi thay đổi:", soup.find("p", class_="footer").get_text(), "\n")

print("=== 5. Thay đổi tên học viên ===")
for li in soup.find_all("li"):
    if li.string == "Trần Uy": li.string = "Trần Uy (Xuất sắc)"
print(*["- "+li.get_text() for li in soup.find_all("li")], sep="\n", end="\n\n")

print("=== 6. Encode & Decode ===")
text = "こんにちは, 私はプログラマーです😊"
encoded = text.encode()
print("Chuỗi encode UTF-8:", encoded)
print("Chuỗi decode lại:", encoded.decode())
