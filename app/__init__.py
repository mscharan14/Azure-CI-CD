from flask import Flask
from .models import init_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='todo.sqlite',
    )

    init_db(app)

    from .api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from .web import bp as web_bp
    app.register_blueprint(web_bp)

    return app
