import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def add_attachment(msg, file_path):
    with open(file_path, 'rb') as file:
        part = MIMEApplication(file.read(), Name=file_path.split("/")[-1])
    part['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
    msg.attach(part)


def send_email(sender, password, subject, body, file_paths, recipient):
    msg = MIMEMultipart('mixed')
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for path in file_paths:
        add_attachment(msg, path)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


if __name__ == '__main__':
    sender = 'sender@gmail.com'
    password = 'Password'  # Be cautious with plaintext passwords
    subject = 'Tere'
    body = """Tere

--
Tere
"""

    file_paths = ['attachments/text2.txt', 'attachments/text1.txt']
    recipients = [line.strip() for line in open("emails.txt")]

    for recipient in recipients:
        send_email(sender, password, subject, body, file_paths, recipient)
