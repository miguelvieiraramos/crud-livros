from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from crud_livros.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from crud_livros.autores.rotas import autores
    from crud_livros.livros.rotas import livros
    from crud_livros.main.rotas import main

    app.register_blueprint(autores)
    app.register_blueprint(livros)
    app.register_blueprint(main)
    return app
