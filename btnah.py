import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    titles = []
    prices = []
    page = 1
    max_pages = 10  # Số trang tối đa để tránh loop vô hạn
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    while page <= max_pages:
        url = base_url.format(page)
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            # Kiểm tra nếu trang không tồn tại
            if response.status_code == 404:
                print(f"Trang {page} không tồn tại. Dừng scraping.")
                break
                
            if response.status_code != 200:
                print(f"Lỗi HTTP {response.status_code} tại trang {page}")
                break
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Kiểm tra có sách trên trang không
            books = soup.find_all('article', class_='product_pod')
            if not books:
                print(f"Không tìm thấy sách trên trang {page}. Dừng scraping.")
                break
                
            for book in books:
                try:
                    title = book.h3.a['title']
                    price = book.find('p', class_='price_color').text
                    titles.append(title)
                    prices.append(price)
                except Exception as e:
                    print(f"Lỗi khi trích xuất dữ liệu sách: {e}")
                    continue
            
            print(f"Đã scrape trang {page}")
            
            # Kiểm tra nút next page
            next_button = soup.select_one('li.next a')
            if not next_button:
                print("Đã đến trang cuối cùng.")
                break
                
            page += 1
            time.sleep(1)  # Nghỉ 1 giây giữa các request
            
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối tại trang {page}: {e}")
            break
    
    return titles, prices

def main():
    print("Bắt đầu scraping...")
    titles, prices = scrape_books()
    
    # Tạo DataFrame và lưu CSV
    df = pd.DataFrame({
        'Title': titles,
        'Price': prices
    })
    
    df.to_csv('books.csv', index=False, encoding='utf-8')
    print(f"Đã lưu {len(df)} quyển sách vào books.csv")

if __name__ == '__main__':
    main()