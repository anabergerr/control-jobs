from flask import Flask
from .extensions import db

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)

    # ... (Registrar Blueprints, configurar rotas, etc)

    return app
