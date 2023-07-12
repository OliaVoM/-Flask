import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_mail(email, subject, text): # записать три параметра функции, формируем сообщение, потом прикрепляем его к серверу
    addr_from = os.getenv('FROM') # в addr_form считает FROM
    password = os.getenv('PASSWORD')
    msg = MIMEMultipart() # создаем объект(это конструктор, поэтому ставим скобки), кот. будет управлять нашими сообщениями
    msg['From'] = addr_from  # сюда пишем тот адрес, кот считали с addr_form
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    server = smtplib.SMTP_SSL(os.getenv('HOST'), os.getenv('PORT'))
    msg.attach(MIMEText(body, 'plain'))  # addr_from приаттачиваем сообщение в телу, кот. только что сделали

    server.starttls()
    server.login(addr_from, password)  # залогинится на сервере
    server.send_message(msg)  # в итоге это сообщение msg отправили
    server.quit()  # выходим с сервера он нам больше не нужен
    return True
