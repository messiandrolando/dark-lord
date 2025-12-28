from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>Giới thiệu về em</title>
</head>
<body>
<h1>Chào mừng đến với trang cá nhân của em</h1>

<div class="post" id="post-1">
<h2>Kỹ năng: Lập trình Python</h2>
<p class="author">Tên: anh tuan</p>
<p class="content">ky nang: tam on</p>
</div>

<div class="post" id="post-2">
<h2>Sở thích: choi game </h2>
<p class="author">Tên: anh tuan</p>
<p class="content">so thich:ko bik</p>
</div>

<div class="post" id="post-3">
<h2>Sở thích: choi game </h2>
<p class="author">Tên: anh tuan</p>
<p class="content">so thich:ko bik</p>
</div>

<table id="users">
<tr><th>Tên</th><th>Tuổi</th><th>Quốc gia</th></tr>
<tr><td>anh tuan</td><td>15</td><td>Việt Nam</td></tr>
</table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

# 1. Tiêu đề trang
title = soup.title.string

# 2. Menu
menu = [a.get_text() for a in soup.select(".menu a")]

# 3. Tiêu đề bài viết
titles = [h2.get_text() for h2 in soup.find_all("h2")]

# 4. Tác giả
authors = [p.get_text().replace("Tác giả: ", "") for p in soup.select("p.author")]

# 5. Link "Đọc thêm" bài viết 2 (rút gọn)
link_post2 = soup.select_one("#post-2 a")
link_post2 = link_post2["href"] if link_post2 else None

# 6. Nội dung content
contents = [p.get_text() for p in soup.select("p.content")]

# In kết quả
print(f"Tiêu đề trang: {title}\n")

print("Menu:")
for m in menu: print(f"    - {m}")
print("\nTiêu đề bài viết:")
for t in titles: print(f"    - {t}")
print("\nTác giả:")
for a in authors: print(f"    - {a}")

print(f"\nLink 'Đọc thêm' bài viết 2: {link_post2}\n")

print("Nội dung các đoạn content:")
for c in contents: print(f"    - {c}")