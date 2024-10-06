from flask import jsonify


def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Aquí puedes añadir más manejadores de errores para otros tipos de excepciones
# Por ejemplo, para errores 404, 500, etc.
