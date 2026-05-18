
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    app.config['SECRET_KEY'] = 'mxnbkedgi rtpogkhe'

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:Manasse05@localhost:5432/contact_manager"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from route import routes
    app.register_blueprint(routes, url_prefix='/')

    from models import User, Contact

    with app.app_context():
        db.create_all()
    login_manager = LoginManager()
    login_manager.login_message = 'S\'il-vous plaît connectez-vous, notre plateforme n\'est plus le même sans vous'
    login_manager.login_view = 'routes.authentified'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app