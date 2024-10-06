from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()
# print(os.getenv('SQLALCHEMY_DATABASE_URI'))
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    
    # Configuración de SMTP
    MAIL_SERVER = os.getenv('SMTP_SERVER')
    MAIL_PORT = int(os.getenv('SMTP_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('SMTP_USERNAME')
    MAIL_PASSWORD = os.getenv('SMTP_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('SMTP_DEFAULT_SENDER')
   