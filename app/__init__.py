from flask import Flask
from flask_cors import CORS
from flask_mail import Mail  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    print("creo la app")
    app.config.from_object('app.config.Config')

    # Inicializar extensiones
    CORS(app, resources={r"*": {"origins": "*"}})
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from app.api.email_api import email_api_blueprint
    from app.api.cena_por_sonrisa_api import cena_bp
    from app.api.countries_api import countries_api_blueprint
    
    app.register_blueprint(countries_api_blueprint, url_prefix='/api')
    app.register_blueprint(email_api_blueprint)
    app.register_blueprint(cena_bp, url_prefix="/api")

    from app.models import country, cena_por_sonrisa
    with app.app_context():
        # db.drop_all() NO descomentar esta linea
        db.create_all()
        from app.services.country_service import CountryService
        CountryService.load_countries()
        
    return app

