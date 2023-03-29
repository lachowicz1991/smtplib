from email.message import EmailMessage
import ssl

import smtplib

p = 'xuklnjrgudhwcmop'

email_sender = 'mlachowicz0509@gmail.com'
password = 'elk12345^'
email_receiver = 'mlachowicz0509@yahoo.com'

subject = 'Happy Birthday'
body = 'All the best'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

contex = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=contex) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())