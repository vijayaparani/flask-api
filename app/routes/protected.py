from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.decorators import role_required

protected_bp = Blueprint("protected", __name__)

@protected_bp.route("/user", methods=["GET"])
@jwt_required()
def user_route():
    return jsonify({"msg": "Hello User"})


@protected_bp.route("/admin", methods=["GET"])
@role_required("admin")
def admin_route():
    return jsonify({"msg": "Hello Admin"})

@protected_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "Flask API is running"
    })