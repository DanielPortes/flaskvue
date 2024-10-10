from app import db
import uuid



class Whisky(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(100), nullable=False)
    distillery = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    region = db.Column(db.String(50))
    tasted = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'distillery': self.distillery,
            'age': self.age,
            'region': self.region,
            'tasted': self.tasted
        }