
from .error_handlers import handle_invalid_usage
from .image_manager import ImageManager

def init_app(app):
    app.register_error_handler(InvalidUsage, handle_invalid_usage)
    # Aquí puedes registrar otros manejadores de errores globales o utilidades comunes

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
