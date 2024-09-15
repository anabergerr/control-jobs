from flask import Flask
from .extensions import db
from .views import job 

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(job, url_prefix='/jobs')

    return app

