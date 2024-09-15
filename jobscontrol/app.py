from flask import Flask
from app import extensions
from config import config
from app.views import job
import os

app = Flask(__name__)

# Configura as configurações da aplicação
config_name = os.getenv('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])

# # Inicializa as extensões
extensions.init_app(app)

# ... (Registrar rotas e outras configurações)


if __name__ == '__main__':
    app.run(debug=True)