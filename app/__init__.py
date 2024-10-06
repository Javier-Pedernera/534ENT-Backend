from flask import Flask
from flask_cors import CORS
from flask_mail import Mail  # Importar Mail

mail = Mail()  # Inicializar Mail

def create_app():
    app = Flask(__name__)
    print("creo la app")
    app.config.from_object('app.config.Config')

    CORS(app, resources={r"*": {"origins": "*"}})
    
    mail.init_app(app)  # Inicializar Mail con la aplicación

    # Registrar blueprints
    from app.api.email_api import email_api_blueprint
    app.register_blueprint(email_api_blueprint)

    return app


#para la futura utilizacion de la base de datos
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask_migrate import Migrate

# # Instancia de SQLAlchemy
# db = SQLAlchemy()

# def create_app():
#     # Crear una instancia de Flask
#     app = Flask(__name__)
#     print("creo la app")
#     # Configuración de la aplicación
#     app.config.from_object('config.Config')
    
#     # Inicializar SQLAlchemy con la aplicación Flask
#     db.init_app(app)
    
#     # Inicializar Flask-Migrate con la aplicación Flask y la instancia de SQLAlchemy
#     migrate = Migrate(app, db)
    
#     # Habilitar CORS si es necesario
#     CORS(app, resources={r"*": {"origins": "*"}})

#     # Importar e inicializar las rutas de la API

#     from app.auth import auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     from app.api.promotions_api import promotion_api_blueprint
#     app.register_blueprint(promotion_api_blueprint)

#     from app.api.category_api import category_api_blueprint
#     app.register_blueprint(category_api_blueprint)

#     from app.api.role_api import role_api_blueprint
#     app.register_blueprint(role_api_blueprint)

#     from app.api.funcionalty_api import functionality_api_blueprint
#     app.register_blueprint(functionality_api_blueprint)

#     from app.api.tourist_api import tourist_api_blueprint
#     app.register_blueprint(tourist_api_blueprint)

#     from app.api.partner_api import partner_api_blueprint
#     app.register_blueprint(partner_api_blueprint)

#     from app.api.favorite_api import favorite_api_blueprint
#     app.register_blueprint(favorite_api_blueprint)
    
#     from app.api.branches_api import branch_api_blueprint
#     app.register_blueprint(branch_api_blueprint)
    
#     from app.api.tourist_point_api import tourist_point_api_blueprint
#     app.register_blueprint(tourist_point_api_blueprint)
    
#     from app.api.branch_rating_api import branch_rating_api_blueprint
#     app.register_blueprint(branch_rating_api_blueprint)

#     from app.api.tourist_rating_api import tourist_rating_api_blueprint
#     app.register_blueprint(tourist_rating_api_blueprint)
    
#     from app.api.countries_api import countries_api_blueprint
#     app.register_blueprint(countries_api_blueprint)

#     from app.api.role_funcionality_api import role_functionality_api_blueprint
#     app.register_blueprint(role_functionality_api_blueprint)

#     from app.api.user_role_api import user_role_api_blueprint
#     app.register_blueprint(user_role_api_blueprint)
    
#     from app.api.status_api import status_api_blueprint
#     app.register_blueprint(status_api_blueprint)
    
#     from app.api.promotion_consumed_api import promotion_consumed_api_blueprint
#     app.register_blueprint(promotion_consumed_api_blueprint)
    
#     from app.api.terms_and_conditions_api import terms_and_conditions_api_blueprint
#     app.register_blueprint(terms_and_conditions_api_blueprint)
#     # Importar modelos para asegurarse de que se reconocen al crear la base de datos
    
#     from app.models import user, category, tourist, partner, promotion, branch, favorite, funcionality, role_funcionality, user_role, status, promotion_consumed

#     # Importar e inicializar los manejadores de errores
#     # from app.common import error_handlers
#     # error_handlers.init_app(app)
    
#     with app.app_context():
#         # db.drop_all()
#         db.create_all()
#         from app.services.country_service import CountryService
#         from app.services.status_load_service import StatusLoadService
#         CountryService.load_countries()
#         StatusLoadService.load_statuses()

#     return app
