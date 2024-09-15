from flask import Flask
from config import Config
from models import db, Job
from routes import bp as routes_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)
