from flask import Flask
from .routes.auth.auth import bp as auth_bp
from .routes.main import bp as main_bp

app = Flask(__name__)


def crear_app():
    
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    
    
    
    
    
    return app