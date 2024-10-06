import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask import render_template, current_app

def send_email(subject, recipients, html_body, pdf_buffer=None, pdf_filename=None):
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = current_app.config['SMTP_DEFAULT_SENDER']
    msg['To'] = ", ".join(recipients)

    part1 = MIMEText(html_body, 'html')
    msg.attach(part1)

    if pdf_buffer and pdf_filename:
        part2 = MIMEApplication(pdf_buffer.read(), _subtype="pdf")
        part2.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
        msg.attach(part2)

    with smtplib.SMTP(current_app.config['SMTP_SERVER'], current_app.config['SMTP_PORT']) as server:
        server.starttls()
        server.login(current_app.config['SMTP_USERNAME'], current_app.config['SMTP_PASSWORD'])
        server.sendmail(current_app.config['SMTP_DEFAULT_SENDER'], recipients, msg.as_string())
