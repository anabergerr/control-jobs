from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importe as configurações do config.py

app = Flask(__name__)
app.config.from_object(Config)  # Carregue as configurações da aplicação

db = SQLAlchemy(app)  # Inicialize o SQLAlchemy com a aplicação

# Importe seus recursos da API aqui
from api.views import JobResource

# Adicione seus endpoints à API
api = Api(app)
api.add_resource(JobResource, '/create')

# Crie as tabelas do banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)