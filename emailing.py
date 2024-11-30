import smtplib
import ssl
from email.mime.text import MIMEText


def send_email(message):
    host="smtp.gmail.com"
    port=465

    username = "p.nikul1603@gmail.com"
    password = "seyg bjen esmg kndm"

    receiver = "p.nikul1603@gmail.com"
    context = ssl.create_default_context()

    subject = "Today's News Update"
    msg = MIMEText(message.decode('utf-8'), "plain")
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] =subject

    with smtplib.SMTP_SSL(host,port, context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver, msg.as_string())

