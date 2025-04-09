from flask import Flask
from .database import connect_db
from .routes import tasks_bp


def create_app():
    app = Flask(__name__)
    connect_db(app)
    app.register_blueprint(tasks_bp)

    return app
