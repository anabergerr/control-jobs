from flask import Flask

from app.models import db
from app.routes.jobs import jobs_bp as routes_dp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes_dp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
