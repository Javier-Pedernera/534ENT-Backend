from app import create_app

app = create_app()

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    # Aquí puedes configurar opciones adicionales para la ejecución del servidor
    # como el puerto, el modo de depuración, etc.
    app.run(host='0.0.0.0', port=7500, debug=True)  # Cambia debug a False en un entorno de producción
