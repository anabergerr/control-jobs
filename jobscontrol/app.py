<<<<<<< HEAD
from app import create_app

app = create_app()
=======
from flask import Flask
from config import Config
from app.models import db, Job
from app.routes.job_create import bp as routes_bp
from app.routes.get_job import bp as get_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes_bp)
app.register_blueprint(get_bp)

>>>>>>> 88e15a0cd1d5e9573276a4f79c1b5b0acfa0288b

if __name__ == '__main__':
    app.run(debug=True)