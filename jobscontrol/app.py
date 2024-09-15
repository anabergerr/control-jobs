from flask import Flask
from flask_restx import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

# Importe seus recursos da API aqui
from api.resources import MyResource

# Adicione seus endpoints à API
api.add_resource(MyResource, '/my_resource')


if __name__ == '__main__':
    app.run(debug=True)

