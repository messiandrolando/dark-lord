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
soup = BeautifulSoup(html_doc, "html.parser")

print("=== 1. find() ===")
first_p = soup.find("p")
print("Thẻ <p> đầu tiên:", first_p.get_text())

content_p = soup.find("p", id="content")
print("Thẻ <p id='content'>:", content_p.get_text())
print()

print("=== 2. find_all() ===")
langs = soup.find_all("li")
print("Danh sách ngôn ngữ:")
for li in langs:
    print("-", li.get_text())

print("\n2 phần tử đầu tiên:")
for li in langs[:2]:
    print("-", li.get_text())
print()

print("=== 3. prettify() ===")
print(soup.prettify())
print()

print("=== 4. replace_with() ===")
footer = soup.find("p", class_="footer")
footer.string.replace_with("Liên hệ quản trị viên")
print("Footer sau khi thay đổi:", footer.get_text())
print()

print("=== 5. Thay đổi tên học viên ===")
students = soup.find_all("li")
for li in students:
    if li.string == "Trần Uy":
        li.string = "Trần Uy (Xuất sắc)"
        break
for li in students:
    print("-", li.get_text())
print()

print("=== 6. Encode & Decode ===")
text = "こんにちは, 私はプログラマーです😊"
encoded = text.encode("utf-8")
print("Chuỗi encode UTF-8 (bytes):", encoded)

decoded = encoded.decode("utf-8")
print("Chuỗi decode lại:", decoded)
