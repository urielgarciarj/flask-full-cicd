from flask import Flask

# Routes
from .routes import Indexroutes, Listusers

app = Flask(__name__)

def init_app():
    # Blueprints
    app.register_blueprint(Indexroutes.main, url_prefix='/')
    app.register_blueprint(Listusers.main, url_prefix='/list')

    return app