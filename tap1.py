"""
HỆ THỐNG GỬI EMAIL ĐƠN GIẢN
Chỉ cần 1 file Python để chạy mọi thứ
"""

import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Tải cấu hình từ .env
load_dotenv("apppasswork/.env")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_SENDER or not EMAIL_PASSWORD:
    print("❌ Lỗi: Không tìm thấy EMAIL_SENDER hoặc EMAIL_PASSWORD trong .env")
    exit(1)

# ========== CẤU HÌNH SMTP ==========
SMTP_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
}

# ========== DANH SÁCH NGƯỜI NHẬN ==========
# Sử dụng thumoisukien.json (dựa trên tài liệu bạn cung cấp)
try:
    with open('thumoisukien.json', 'r', encoding='utf-8') as f:
        RECIPIENTS = json.load(f)
except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy thumoisukien.json")
    exit(1)

# ========== TEMPLATE EMAIL ==========
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thư Mời Sự Kiện</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f4; font-family: 'Times New Roman', Times, serif;">
    
    <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                
                <div style="
                    max-width: 600px; 
                    background-color: #fffdf5; 
                    border: 1px solid #d4af37; 
                    padding: 5px; 
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    margin: 0 auto;">
                    
                    <div style="
                        border: 3px double #d4af37; 
                        padding: 30px 20px; 
                        text-align: center;
                        color: #5d4037;">

                        <div style="margin-bottom: 20px;">
                            <h3 style="color: #2ecc71; display: inline-block; margin: 0 10px;">CCBOOK</h3>
                            <h3 style="color: #f1c40f; display: inline-block; margin: 0 10px;">CC THẦN TỐC</h3>
                        </div>

                        <div style="font-size: 20px; color: #d4af37; margin-bottom: 10px;">⚜</div>

                        <h1 style="
                            font-size: 28px; 
                            margin: 10px 0; 
                            text-transform: uppercase; 
                            color: #5d4037; 
                            letter-spacing: 1px;
                            line-height: 1.4;">
                            Thư Mời<br>Tham Gia Sự Kiện
                        </h1>

                        <div style="font-size: 20px; color: #d4af37; margin-bottom: 30px;">⚜</div>

                        <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            Trân trọng kính mời <strong>{name}</strong> và quý khách hàng đến tham dự:<br>
                            <em>Lễ ra mắt bộ sách "CC Thần tốc luyện đề chinh phục kì thi THPT QG 2020"</em>
                        </p>

                        <div style="margin: 25px 0;">
                            <span style="
                                background-color: #5d4037; 
                                color: #ffffff; 
                                padding: 10px 30px; 
                                border-radius: 50px; 
                                font-weight: bold; 
                                font-size: 18px;
                                display: inline-block;">
                                <strong>{time}</strong> | <strong>{date}</strong>
                            </span>
                        </div>

                        <p style="font-size: 15px; margin-bottom: 40px; color: #5d4037;">
                            <strong>Hội trường Tầng 1, Cung Trí Thức</strong><br>
                            Số 1 Tôn Thất Thuyết - Phường Dịch Vọng - Cầu Giấy - Hà Nội
                        </p>

                        <div style="
                            border-top: 1px solid #d4af37; 
                            padding-top: 20px; 
                            font-size: 12px; 
                            color: #666; 
                            display: flex; 
                            justify-content: space-between;
                            flex-wrap: wrap;">
                            
                            <div style="text-align: left; width: 48%; min-width: 200px; margin-bottom: 10px;">
                                <strong>Công ty Cổ phần CCGroup Toàn Cầu</strong><br>
                                Số 10 Dương Quảng Hàm - Cầu Giấy - Hà Nội
                            </div>
                            
                            <div style="text-align: right; width: 48%; min-width: 200px;">
                                <strong>Xác nhận tham gia sự kiện với:</strong><br>
                                Ms. Phương 0779251059
                            </div>
                        </div>

                    </div>
                </div>
                </td>
        </tr>
    </table>
</body>
</html>
"""

def send_email(to_name, to_email, subject, to_time="", to_date=""):
    """Gửi một email đơn giản"""
    
    # Chuẩn bị nội dung email
    html_content = HTML_TEMPLATE.replace("{name}", to_name)
    html_content = html_content.replace("{time}", to_time)
    html_content = html_content.replace("{date}", to_date)
    
    try:
        # Tạo email
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL_SENDER
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Thêm nội dung HTML
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Kết nối và gửi email
        with smtplib.SMTP(SMTP_CONFIG['smtp_server'], SMTP_CONFIG['smtp_port']) as server:
            server.starttls()  # Bảo mật kết nối
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Đã gửi email đến: {to_name} ({to_email})")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print(f"❌ Lỗi xác thực! Kiểm tra email và mật khẩu trong .env.")
        return False
    except Exception as e:
        print(f"❌ Lỗi khi gửi email đến {to_email}: {str(e)}")
        return False

def main():
    """Hàm chính - chạy chương trình"""
    
    print("=" * 50)
    print("📧 HỆ THỐNG GỬI EMAIL ĐƠN GIẢN")
    print("=" * 50)
    
    # Hiển thị thông tin cấu hình
    print(f"\n📋 THÔNG TIN CẤU HÌNH:")
    print(f"   Email gửi: {EMAIL_SENDER}")
    print(f"   SMTP Server: {SMTP_CONFIG['smtp_server']}:{SMTP_CONFIG['smtp_port']}")
    print(f"   Số người nhận: {len(RECIPIENTS)}")
    
    # Xác nhận trước khi gửi
    confirm = input("\n⚠️  Bạn có muốn bắt đầu gửi email không? (y/n): ")
    if confirm.lower() != 'y':
        print("Đã hủy gửi email.")
        return
    
    # Tiêu đề email
    subject = "Thư mời tham gia sự kiện - CCBook & CC Thần Tốc"
    
    # Gửi email cho từng người
    print(f"\n🚀 Bắt đầu gửi {len(RECIPIENTS)} email...\n")
    
    success_count = 0
    for person in RECIPIENTS:
        if send_email(person['name'], person['email'], subject, person.get('time', ''), person.get('date', '')):
            success_count += 1
    
    # Hiển thị kết quả
    print(f"\n" + "=" * 50)
    print("📊 KẾT QUẢ:")
    print(f"   Tổng số: {len(RECIPIENTS)} email")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {len(RECIPIENTS) - success_count}")
    print("=" * 50)

if __name__ == "__main__":
    main()
