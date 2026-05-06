from flask import Blueprint
from flask import request
from flask import jsonify

from app.services.auth_service import AuthService
from app.utils.validators import validate_register_data

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    try:

        data = request.get_json()

        validate_register_data(
            data
        )

        user = AuthService.register(
            data
        )

        return jsonify({
            "success": True,
            "message": "User created",
            "username": user.username
        }), 201

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400


@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    try:

        data = request.get_json()

        token = AuthService.login(
            data
        )

        return jsonify({
            "success": True,
            "token": token
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 401