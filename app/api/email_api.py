from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.email_service import send_email

# Crear Blueprint para el módulo de emails
email_api_blueprint = Blueprint('email_api', __name__)
api = Api(email_api_blueprint)

# Recurso para manejo de un email específico
class EmailResource(Resource):
    def post(self):
        data = request.get_json()
        
        required_fields = ['recipient', 'subject', 'username', 'email', 'company', 'message', 'title']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        recipient = data.get('recipient')
        subject = data.get('subject')
        username = data.get('username')
        email = data.get('email')
        company = data.get('company')
        message = data.get('message')
        title = data.get('title')
        
        try:
            send_email(
                recipient, 
                subject, 
                'email/email-entertainment.html',
                title=title,
                username=username,
                email=email,
                company=company,
                message=message
            )
            return {'message': 'Email sent successfully!'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

# Registrar rutas para los emails específicos
api.add_resource(EmailResource, '/send-email-534ent')
