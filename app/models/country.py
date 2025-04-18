from app import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    code = db.Column(db.String(3), nullable=True)
    phone_code = db.Column(db.String(10), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'phone_code': self.phone_code 
        }