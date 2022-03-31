from flask import Flask
from app.blueprints import home
from app.extensions import db, migrate, admin, babel, websocket


def create_app(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)

    # Extensions
    db.configure(app)
    migrate.configure(app)
    admin.configure(app)
    websocket.configure(app)
    babel.configure(app)

    # Blueprints
    home.configure(app)

    return app