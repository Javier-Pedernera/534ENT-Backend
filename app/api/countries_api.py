from flask import Blueprint, jsonify
from app.services.country_service import CountryService

countries_api_blueprint = Blueprint('countries_api', __name__)

@countries_api_blueprint.route('/countries', methods=['GET'])
def obtener_paises():
    countries = CountryService.get_all_countries()
    return jsonify([country.serialize() for country in countries])