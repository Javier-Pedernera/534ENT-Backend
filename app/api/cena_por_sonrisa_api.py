from flask import Blueprint, request, jsonify
from app.services.cena_por_sonrisa_service import guardar_formulario_cena

cena_bp = Blueprint('cena', __name__)

@cena_bp.route('/cena_por_una_sonrisa', methods=['POST'])
def enviar_formulario_cena():
    data = request.json

    campos_requeridos = ['nombre','apellido', 'email', 'pais_id']
    
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({'error': f'Campo requerido faltante: {campo}'}), 400

    reserva = guardar_formulario_cena(data)
    return jsonify({'mensaje': 'Formulario guardado con éxito', 'id': reserva.id}), 201