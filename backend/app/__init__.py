from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config
from app.utils.error_handlers import register_error_handlers
from app.resources.swagger import setup_swagger


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.routes.whisky_routes import whisky_routes
    app.register_blueprint(whisky_routes)

    register_error_handlers(app)
    setup_swagger(app)

    return app