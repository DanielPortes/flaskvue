from app import db
from app.models.whisky import Whisky

class WhiskyService:
    @staticmethod
    def get_all_whiskies():
        return Whisky.query.all()

    @staticmethod
    def create_whisky(whisky_data):
        new_whisky = Whisky(**whisky_data)
        db.session.add(new_whisky)
        db.session.commit()
        return new_whisky

    @staticmethod
    def get_whisky_by_id(whisky_id):
        return Whisky.query.get_or_404(whisky_id)

    @staticmethod
    def update_whisky(whisky, whisky_data):
        for key, value in whisky_data.items():
            setattr(whisky, key, value)
        db.session.commit()
        return whisky

    @staticmethod
    def delete_whisky(whisky):
        db.session.delete(whisky)
        db.session.commit()