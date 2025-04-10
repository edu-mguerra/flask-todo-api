from flask import Flask
from .database import connect_db  # importamos a conexão com o banco de dados
from .routes import tasks_bp


def create_app():
    app = Flask(__name__)
    connect_db(app)  # conecta o app ao banco de dados
    app.register_blueprint(tasks_bp)  #  Registra o Blueprint com as rotas da API

    return app
