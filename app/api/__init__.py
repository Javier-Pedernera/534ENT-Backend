from flask import Blueprint
from app.api.cena_por_sonrisa_api import cena_bp

def register_routes(app):
    app.register_blueprint(cena_bp)