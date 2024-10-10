import pytest
from app import create_app, db
from app.models.whisky import Whisky
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    with app.app_context():
        whisky = Whisky(name="Jack Daniels", type="Bourbon", proof=80)
        db.session.add(whisky)
        db.session.commit()
        yield
