"""
🎉 HỆ THỐNG GỬI EMAIL CHÚC MỪNG SINH NHẬT HOÀN CHỈNH
Tác giả: Hệ thống tự động
Ngày tạo: 2024
"""

import smtplib
import json
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import getpass
from dotenv import load_dotenv

# Load biến từ file .env
load_dotenv("C:\\module_python\\apppasswork\\.env")

class BirthdayEmailSystem:
    """Hệ thống gửi email chúc mừng sinh nhật"""
    
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.sender_email = os.getenv("EMAIL_SENDER", "tuanbui.ttv@gmail.com")
        self.sender_password = os.getenv("EMAIL_PASSWORD", "")
        self.recipients = []
        self.html_template = "C:\\module_python\\emails_template\\html_template\\text.html"
        
    def display_banner(self):
        """Hiển thị banner hệ thống"""
        print("\n" + "="*70)
        print("🎂 HỆ THỐNG GỬI EMAIL CHÚC MỪNG SINH NHẬT")
        print("="*70)
        print("📧 Gửi email tự động đến nhiều người cùng lúc")
        print("🎁 Cá nhân hóa với tên từng người nhận")
        print("📊 Theo dõi kết quả gửi chi tiết")
        print("="*70)
    
    def setup_email_config(self):
        """Thiết lập cấu hình email"""
        print("\n🔧 THIẾT LẬP CẤU HÌNH EMAIL GỬI")
        print("-"*50)
        
        # Nhập email
        
        
        # Nhập mật khẩu (ẩn mật khẩu khi nhập)
        
        
        # Kiểm tra thông tin cơ bản
        if not self.sender_password:
            print("❌ Chưa nhập mật khẩu!")
            return False
        
        print(f"✅ Đã thiết lập email gửi: {self.sender_email}")
        return True
    
    def select_file(self, file_type, default_file):
        """Chọn file template hoặc JSON"""
        print(f"\n📁 CHỌN FILE {file_type.upper()}:")
        print(f"   📍 File mặc định: {default_file}")
        
        # Kiểm tra file mặc định
        if os.path.exists(default_file):
            print(f"   ✅ File tồn tại ({os.path.getsize(default_file)} bytes)")
        else:
            print(f"   ⚠️  File không tồn tại - sẽ tạo file mẫu")
        
        # Cho phép chọn file khác
        choice = input(f"   Nhấn Enter để dùng file trên, hoặc nhập đường dẫn file mới: ").strip()
        
        selected_file = choice if choice else default_file
        
        # Nếu file không tồn tại, tạo file mẫu
        if not os.path.exists(selected_file):
            self.create_sample_file(selected_file, file_type)
        
        return selected_file
    
    def create_sample_file(self, filename, file_type):
        """Tạo file mẫu nếu không tồn tại"""
        try:
            if file_type == "template":
                sample_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chúc Mừng Sinh Nhật</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #ffffff;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            background-color: #f0f0f0;
            padding: 20px;
            text-align: center;
        }
        .logo {
            width: 350p;
        }
        .banner {
            width: 100%;
            height: auto;
        }
        .content {
            padding: 20px;
            text-align: left;
            color: #333333;
        }
        .greeting {
            font-size: 18px;
            margin-bottom: 20px;
        }
        .message {
            font-size: 16px;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .signature {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .illustration {
            text-align: center;
            margin-bottom: 20px;
        }
        .illustration img {
            max-width: 100%;
            height: auto;
        }
        .footer-banner {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Phần đầu với Logo -->
        <div class="header">
            <img src="https://media-cdn-v2.laodong.vn/storage/newsportal/2022/9/14/1092939/Logo-Moi.jpg" alt="Logo VietnamWorks" class="logo">
            
        </div>

        <!-- Banner trên cùng (hình vẽ sinh nhật hoặc confetti) -->
        
        <!-- Nội dung -->
        <div class="content">
            <p class="greeting">Xin chào [name],</p>
            <p class="message">
                Hôm nay là một ngày đặc biệt. Thay vì công việc, chúng tôi muốn gửi lời CHÚC MỪNG SINH NHẬT đến bạn. Câu chúc cho bạn một năm tuyệt vời với những cơ hội mới, thành công và phát triển mới.
            </p>
            <p class="signature">
                VietnamWorks - Chúc bạn một ngày sinh nhật vui vẻ và Phất Triển!
            </p>
        </div>
        <!-- Banner chân trang (hình vẽ sinh nhật tương tự) -->
        <img src="https://media.istockphoto.com/id/1306306868/vi/vec-to/n%E1%BB%81n-t%E1%BA%A3ng-ti%E1%BB%87c-v%E1%BA%BD-tay-vui-nh%E1%BB%99n-v%E1%BB%9Bi-b%C3%A1nh-ng%E1%BB%8Dt-h%E1%BB%99p-qu%C3%A0-b%C3%B3ng-bay-v%C3%A0-trang-tr%C3%AD-b%E1%BB%AFa-ti%E1%BB%87c-tuy%E1%BB%87t-v%E1%BB%9Di.jpg?s=612x612&w=0&k=20&c=4FfRjgmg8MunZZt3_7x7pICK9BexR996UeXgSPxSVSg=" alt="Hình vẽ Sinh Nhật" class="footer-banner">
    </div>
</body>
</html>"""
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(sample_content)
                print(f"✅ Đã tạo file template mẫu: {filename}")
                
            elif file_type == "json":
                sample_content = [
                    
                    {
                        "name": "Anh Tuấn",
                        "email": "tuanbui.ttv@gmail.com"
                    }
                    
                ]
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(sample_content, f, ensure_ascii=False, indent=2)
                print(f"✅ Đã tạo file danh sách mẫu: {filename}")
                
        except Exception as e:
            print(f"❌ Lỗi khi tạo file mẫu: {e}")
    
    def load_files(self):
        """Đọc template và danh sách người nhận"""
        print("\n📂 ĐANG TẢI DỮ LIỆU...")
        print("-"*50)
        
        # Chọn và đọc template
        template_file = self.select_file("template", "birthday_template.html")
        
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                self.html_template = f.read()
            print(f"✅ Đã tải template từ: {template_file}")
            print(f"   Kích thước: {len(self.html_template)} ký tự")
        except Exception as e:
            print(f"❌ Lỗi khi đọc template: {e}")
            return False
        
        # Chọn và đọc danh sách người nhận
        json_file = self.select_file("json", "birthday_recipients.json")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                self.recipients = json.load(f)
            print(f"✅ Đã tải danh sách từ: {json_file}")
            print(f"   Số người nhận: {len(self.recipients)}")
        except Exception as e:
            print(f"❌ Lỗi khi đọc danh sách: {e}")
            return False
        
        # Kiểm tra có người nhận không
        if not self.recipients:
            print("❌ Không có người nhận nào trong danh sách!")
            return False
        
        # Hiển thị danh sách người nhận
        print("\n👥 DANH SÁCH NGƯỜI NHẬN:")
        print("-"*60)
        for i, person in enumerate(self.recipients, 1):
            name = person.get('name', 'Không có tên')
            email = person.get('email', 'Không có email')
            print(f"   {i:3d}. {name:25s} - {email}")
        
        return True
    
    def customize_email_content(self, name):
        """Cá nhân hóa nội dung email"""
        # Thay thế {name} trong template bằng tên thật
        content = self.html_template.replace("{name}", name)
        
        # Có thể thêm các thay thế khác nếu cần
        content = content.replace("[hưng]", name)
        
        return content
    
    def send_single_email(self, recipient):
        """Gửi email đến một người"""
        name = recipient.get('name', 'Bạn')
        email = recipient.get('email', '')
        
        if not email or '@' not in email:
            print(f"❌ Email không hợp lệ: {email}")
            return False, "Email không hợp lệ"
        
        try:
            # Cá nhân hóa nội dung
            html_content = self.customize_email_content(name)
            
            # Tạo email
            msg = MIMEMultipart('alternative')
            msg['From'] = self.sender_email
            msg['To'] = email
            msg['Subject'] = f"🎂 Chúc Mừng Sinh Nhật {name}!"
            
            # Thêm nội dung HTML
            msg.attach(MIMEText(html_content, 'html'))
            
            # Kết nối và gửi email
            print(f"   🔗 Kết nối đến {self.smtp_server}:{self.smtp_port}...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            return True, "Gửi thành công"
            
        except smtplib.SMTPAuthenticationError:
            return False, "Lỗi xác thực: Sai email/mật khẩu"
        except smtplib.SMTPException as e:
            return False, f"Lỗi SMTP: {e}"
        except Exception as e:
            return False, f"Lỗi: {str(e)}"
    
    def send_all_emails(self):
        """Gửi email cho tất cả người nhận"""
        print("\n🚀 BẮT ĐẦU GỬI EMAIL...")
        print("="*70)
        
        results = []
        success_count = 0
        
        for i, recipient in enumerate(self.recipients, 1):
            name = recipient.get('name', f"Người nhận {i}")
            email = recipient.get('email', '')
            
            print(f"\n📨 [{i}/{len(self.recipients)}] Đang gửi cho: {name}")
            print(f"   📧 Email: {email}")
            
            # Gửi email
            start_time = datetime.now()
            success, message = self.send_single_email(recipient)
            elapsed = (datetime.now() - start_time).total_seconds()
            
            if success:
                print(f"   ✅ Thành công ({elapsed:.1f}s)")
                success_count += 1
            else:
                print(f"   ❌ Thất bại: {message}")
            
            results.append({
                'index': i,
                'name': name,
                'email': email,
                'success': success,
                'message': message,
                'time': elapsed
            })
        
        return results, success_count
    
    def show_results(self, results, success_count):
        """Hiển thị kết quả chi tiết"""
        print("\n" + "="*70)
        print("📊 KẾT QUẢ CHI TIẾT")
        print("="*70)
        
        total = len(results)
        failed_count = total - success_count
        
        print(f"   Tổng số email: {total}")
        print(f"   ✅ Thành công: {success_count} ({success_count/total*100:.1f}%)")
        print(f"   ❌ Thất bại: {failed_count} ({failed_count/total*100:.1f}%)")
        
        # Hiển thị chi tiết từng email
        if failed_count > 0:
            print("\n📋 CHI TIẾT EMAIL THẤT BẠI:")
            for result in results:
                if not result['success']:
                    print(f"   • {result['name']}: {result['message']}")
        
        # Tổng thời gian
        total_time = sum(r['time'] for r in results)
        print(f"\n⏱️  Tổng thời gian: {total_time:.1f} giây")
        print(f"   Trung bình: {total_time/total:.1f} giây/email")
    
    def save_log_file(self, results):
        """Lưu log kết quả vào file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"birthday_email_log_{timestamp}.txt"
            
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write("="*60 + "\n")
                f.write("KẾT QUẢ GỬI EMAIL CHÚC MỪNG SINH NHẬT\n")
                f.write(f"Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Email gửi: {self.sender_email}\n")
                f.write("="*60 + "\n\n")
                
                for result in results:
                    status = "✅ THÀNH CÔNG" if result['success'] else "❌ THẤT BẠI"
                    f.write(f"[{result['index']}] {result['name']}\n")
                    f.write(f"    Email: {result['email']}\n")
                    f.write(f"    Trạng thái: {status}\n")
                    f.write(f"    Thông báo: {result['message']}\n")
                    f.write(f"    Thời gian: {result['time']:.1f}s\n")
                    f.write("-"*40 + "\n")
                
                # Tổng kết
                success_count = sum(1 for r in results if r['success'])
                total = len(results)
                f.write(f"\n📈 TỔNG KẾT:\n")
                f.write(f"   Tổng số: {total}\n")
                f.write(f"   Thành công: {success_count}\n")
                f.write(f"   Thất bại: {total - success_count}\n")
                f.write(f"   Tỷ lệ thành công: {success_count/total*100:.1f}%\n")
            
            print(f"📝 Đã lưu log chi tiết vào: {log_filename}")
            return log_filename
        except Exception as e:
            print(f"❌ Không thể lưu log file: {e}")
            return None
    
    def show_troubleshooting(self, results):
        """Hiển thị hướng dẫn khắc phục sự cố"""
        if any(not r['success'] for r in results):
            print("\n🔧 HƯỚNG DẪN KHẮC PHỤC:")
            print("-"*50)
            print("1. 🚫 Lỗi xác thực (Authentication Failed):")
            print("   • Kiểm tra lại email và mật khẩu")
            print("   • Đảm bảo đã dùng 'App Password', không dùng mật khẩu thường")
            print("   • Kiểm tra xem đã bật 'Xác minh 2 bước' chưa")
            
            print("\n2. 🌐 Lỗi kết nối:")
            print("   • Kiểm tra kết nối Internet")
            print("   • Tường lửa có thể chặn cổng 587")
            print("   • Thử dùng mạng khác nếu có thể")
            
            print("\n3. 📧 Lỗi email:")
            print("   • Kiểm tra định dạng email người nhận")
            print("   • Đảm bảo email tồn tại")
            print("   • Tài khoản Gmail có thể đã hết hạn gửi")
    
    def run(self):
        """Chạy hệ thống"""
        self.display_banner()
        
        # Bước 1: Thiết lập email
        if not self.setup_email_config():
            print("❌ Không thể thiết lập email. Kết thúc chương trình.")
            return
        
        # Bước 2: Tải file template và danh sách
        if not self.load_files():
            print("❌ Không thể tải dữ liệu. Kết thúc chương trình.")
            return
        
        # Xác nhận trước khi gửi
        print(f"\n⚠️  XÁC NHẬN GỬI EMAIL")
        print(f"   Số lượng: {len(self.recipients)} email")
        print(f"   Email gửi: {self.sender_email}")
        print(f"   Tiêu đề: Chúc Mừng Sinh Nhật [Tên người nhận]")
        
        confirm = input("\n   Bạn có chắc chắn muốn gửi? (y/n): ").strip().lower()
        
        if confirm != 'y':
            print("❌ Đã hủy gửi email.")
            return
        
        # Bước 3: Gửi tất cả email
        results, success_count = self.send_all_emails()
        
        # Bước 4: Hiển thị kết quả
        self.show_results(results, success_count)
        
        # Bước 5: Lưu log
        log_file = self.save_log_file(results)
        if log_file:
            print(f"💾 Log đã được lưu vào: {log_file}")
        
        # Bước 6: Hiển thị hướng dẫn khắc phục nếu có lỗi
        if success_count < len(results):
            self.show_troubleshooting(results)
        
        print("\n" + "="*70)
        print("🎉 HOÀN THÀNH HỆ THỐNG GỬI EMAIL!")
        print("="*70)
        print("\nCảm ơn bạn đã sử dụng hệ thống!")
        
        # Hiển thị thông điệp kết thúc
        print("\n📌 LƯU Ý QUAN TRỌNG:")
        print("   • Xóa mật khẩu App Password khỏi bộ nhớ tạm")
        print("   • Không chia sẻ file log chứa thông tin cá nhân")
        print("   • Kiểm tra hộp thư 'Đã gửi' để xác nhận")

def main():
    """Hàm chính"""
    try:
        # Tạo và chạy hệ thống
        system = BirthdayEmailSystem()
        system.run()
        
        # Chờ người dùng nhấn Enter trước khi thoát
        input("\nNhấn Enter để thoát...")
        
    except KeyboardInterrupt:
        print("\n\n❌ Đã hủy bởi người dùng!")
    except Exception as e:
        print(f"\n❌ Lỗi không xác định: {e}")
        input("Nhấn Enter để thoát...")

if __name__ == "__main__":
    main()
