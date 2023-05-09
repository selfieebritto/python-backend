from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.routes import api_bp, health_check_bp

def create_app():
    app = Flask(__name__)
    # Configure JWT settings
    app.config['JWT_SECRET_KEY'] = 'JWT-TOKEN'  # Replace with your own secret key
    jwt = JWTManager(app)
    CORS(app)

    # Register the API Blueprint
    app.register_blueprint(api_bp, url_prefix='/api')
    # Register the health check Blueprint
    app.register_blueprint(health_check_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
