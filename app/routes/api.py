from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import jwt_required

from app.utils.decorators import role_required

api_bp = Blueprint(
    "api",
    __name__
)


@api_bp.route(
    "/health",
    methods=["GET"]
)
def health():

    return jsonify({
        "success": True,
        "message": "API running"
    })


@api_bp.route(
    "/profile",
    methods=["GET"]
)
@jwt_required()
def profile():

    return jsonify({
        "success": True,
        "message": "Authenticated"
    })


@api_bp.route(
    "/admin",
    methods=["GET"]
)
@role_required("admin")
def admin():

    return jsonify({
        "success": True,
        "message": "Welcome Admin"
    })