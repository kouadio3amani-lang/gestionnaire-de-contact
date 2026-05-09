import os
from flask import Flask
def create_app():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    from route import routes
    app.register_blueprint(routes, url_prefix='/')

    return app