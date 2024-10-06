from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_email(recipient, subject, template_name, **template_context):
    html_body = render_template(template_name, **template_context)
    # print(current_app.config['MAIL_DEFAULT_SENDER'])
    # # Crear el mensaje
    # print("Message Subject:", subject)
    # print("Recipients:", [recipient])
    msg = Message(subject, recipients=[recipient], sender=current_app.config['MAIL_DEFAULT_SENDER'])
    msg.html = html_body
    
    # Enviar el correo
    mail.send(msg)