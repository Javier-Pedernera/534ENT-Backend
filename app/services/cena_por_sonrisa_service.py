from app import db
from sqlalchemy.exc import IntegrityError
from app.models.country import Country
from app.models.cena_por_sonrisa import CenaPorUnaSonrisa

def guardar_formulario_cena(data):
    try:
        # Verificar que el 'pais_id' hace referencia a un país existente
        pais = Country.query.get(data['pais_id'])
        if not pais:
            raise ValueError("El país especificado no existe")

        # Separar nombre y apellido
        nombre = data.get('nombre', '')
        apellido = data.get('apellido', '')

        # Crear el objeto de reserva con los campos separados de nombre y apellido
        reserva = CenaPorUnaSonrisa(
            nombre=nombre,
            apellido=apellido,
            direccion=data.get('direccion', ''),
            cena_asistira=data.get('cena_asistira', ''),
            tipo_comida=data.get('tipo_comida', ''),
            cantidad_invitados=data.get('cantidad_invitados', 0),
            nombres_acompanantes=data.get('nombres_acompanantes', ''),
            detalles=data.get('detalles', ''),
            email=data['email'],
            pais_id=pais.id
        )

        db.session.add(reserva)
        db.session.commit()

        return reserva

    except ValueError as e:
        db.session.rollback()
        raise e
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Error al guardar la reserva. Puede que haya un conflicto de integridad.")
