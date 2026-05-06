from flask import Flask
from flask import jsonify

from app.config import Config
from app.extensions import db
from app.extensions import jwt


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.api import api_bp

    app.register_blueprint(
        auth_bp,
        url_prefix="/auth"
    )

    app.register_blueprint(
        api_bp,
        url_prefix="/api"
    )

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "message": "Route not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error"
        }), 500

    with app.app_context():
        db.create_all()

    return app