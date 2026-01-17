import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  # <--- Thêm thư viện xử lý ảnh
from dotenv import load_dotenv

# 1. Tải cấu hình
load_dotenv("apppasswork/.env")
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(student_data, html_template):
    # Sử dụng 'related' để cho phép đính kèm ảnh hiển thị inline
    msg = MIMEMultipart('related') 
    msg['Subject'] = f"GIẤY BÁO DỰ THI ĐGNL - {student_data['ho_ten']}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = student_data['email']

    # --- Phần 1: Xử lý nội dung HTML ---
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    # Thay thế dữ liệu
    html_content = html_template
    replacements = {
        "{{sbd}}": student_data['sbd'],
        "{{ngay_thi}}": student_data['ngay_thi'],
        "{{dia_diem}}": student_data['dia_diem'],
        "{{link_dia_diem}}": student_data['link_dia_diem'],
        "{{phong_thi}}": student_data['phong_thi'],
        "{{ma_ho_so}}": student_data['ma_ho_so'],
        "{{ho_ten}}": student_data['ho_ten'],
        "{{gioi_tinh}}": student_data['gioi_tinh'],
        "{{ngay_sinh}}": student_data['ngay_sinh'],
        "{{noi_sinh}}": student_data['noi_sinh'],
        "{{cccd}}": student_data['cccd'],
        "{{ngay_cap}}": student_data['ngay_cap'],
        "{{noi_cap}}": student_data['noi_cap'],
        "{{dia_chi}}": student_data['dia_chi'],
        "{{sdt}}": student_data['sdt'],
        "{{email_lien_lac}}": student_data['email_lien_lac']
    }

    for key, value in replacements.items():
        html_content = html_content.replace(key, str(value))

    # Đính kèm HTML vào email
    msg_alternative.attach(MIMEText(html_content, 'html'))

    # --- Phần 2: Xử lý Logo ĐHQG (QUAN TRỌNG) ---
    try:
        # Mở file ảnh logo.jpg nằm cùng thư mục
        with open('logo.jpg', 'rb') as f:
            img_data = f.read()
        
        # Tạo object ảnh
        image = MIMEImage(img_data)
        
        # Gán Content-ID khớp với src="cid:logo_vnuhcm" trong HTML
        image.add_header('Content-ID', '<logo_vnuhcm>') 
        image.add_header('Content-Disposition', 'inline', filename='logo.jpg')
        
        # Đính kèm ảnh vào email
        msg.attach(image)
        
    except FileNotFoundError:
        print("⚠️ Cảnh báo: Không tìm thấy file logo.jpg. Email sẽ gửi thiếu logo.")

    # --- Gửi email ---
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, student_data['email'], msg.as_string())
        server.quit()
        print(f"✅ Đã gửi thành công cho: {student_data['ho_ten']}")
    except Exception as e:
        print(f"❌ Lỗi khi gửi cho {student_data['ho_ten']}: {str(e)}")

def main():
    # Đọc template
    try:
        with open(r'C:\module_python\emails_template\html_template\giai_chung_tuyen.html', 'r', encoding='utf-8') as f:
            html_template = f.read()
    except FileNotFoundError:
        print("❌ Lỗi: Không tìm thấy file template.html")
        return

    # Đọc data
    try:
        with open(r'C:\module_python\bt ve email\data.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
    except FileNotFoundError:
        print("❌ Lỗi: Không tìm thấy file data.json")
        return

    print("--- BẮT ĐẦU GỬI EMAIL ---")
    for student in students:
        send_email(student, html_template)
    print("--- HOÀN TẤT ---")

if __name__ == "__main__":
    main()