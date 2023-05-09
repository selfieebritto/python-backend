from flask import Flask
from app.routes import api_bp

def create_app():
    app = Flask(__name__)

    # Register the API Blueprint
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
