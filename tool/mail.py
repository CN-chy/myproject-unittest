import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import subprocess
import sys


# 检测并安装库的函数
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


# 检查所需的库并安装
required_packages = ['smtplib', 'email']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} 未安装，正在安装...")
        install(package)

# 导入所需的库
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, attachments_dir):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # 添加HTML正文
    html = '<h1>见附件</h1>'
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    # 添加附件
    for root, dirs, files in os.walk(attachments_dir):
        for file in files:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(open(os.path.join(root, file), 'rb').read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(attachment)
    try:
        # 使用 SSL 连接
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("邮件发送成功！")
    except Exception as e:
        print(f"发送邮件时出错: {e}")
    finally:
        server.quit()
attachments_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/docs'

send_email('495936663@qq.com', 'qudzveekbkcbbigb', '495936663@qq.com', '自动化用例运行情况', attachments_dir)



