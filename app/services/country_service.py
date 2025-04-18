import requests
import time
from requests.exceptions import ChunkedEncodingError, RequestException
from app import db
from app.models.country import Country


class CountryService:

    @staticmethod
    def load_countries():
        if Country.query.count() > 0:
            print("Los países ya están cargados en la base de datos.")
            return

        url = "https://restcountries.com/v3.1/independent?status=true"
        max_retries = 3  # Número máximo de reintentos
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # Lanza un error si el código de estado no es 2xx
                
                countries_data = response.json()
                countries = sorted(countries_data, key=lambda x: x['name']['common'])

                for country in countries:
                    name = country['name']['common']
                    
                    # Obtener el código del país (por defecto 'UNKNOWN' si no está disponible)
                    code = country.get("cca3", "UNKNOWN")
                    
                    # Construir el código telefónico
                    phone_code = ""
                    if 'idd' in country:
                        if 'root' in country['idd'] and 'suffixes' in country['idd'] and len(country['idd']['suffixes']) > 0:
                            phone_code = country['idd']['root'] + country['idd']['suffixes'][0]

                    # Crear una nueva entrada de país
                    new_country = Country(name=name, code=code, phone_code=phone_code)
                    db.session.add(new_country)

                db.session.commit()
                print("Países cargados exitosamente en la base de datos.")
                return
            
            except ChunkedEncodingError:
                print(f"ChunkedEncodingError: Intento {attempt + 1} de {max_retries}")
            except RequestException as e:
                print(f"Error al realizar la solicitud: {e}")
            
            # Esperar antes de reintentar
            if attempt < max_retries - 1:
                time.sleep(2)

        print("Error: No se pudo cargar la lista de países después de varios intentos.")

    @staticmethod
    def get_all_countries():
        return Country.query.all()