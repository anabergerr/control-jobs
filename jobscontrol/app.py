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


if __name__ == '__main__':
    app.run(debug=True)
