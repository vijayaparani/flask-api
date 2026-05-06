from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models.user import User


class AuthService:

    @staticmethod
    def register(data):

        existing_user = User.query.filter_by(
            username=data["username"]
        ).first()

        if existing_user:
            raise ValueError(
                "Username already exists"
            )

        user = User(
            username=data["username"],
            role=data.get("role", "user")
        )

        user.set_password(
            data["password"]
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def login(data):

        user = User.query.filter_by(
            username=data["username"]
        ).first()

        if not user:
            raise ValueError(
                "Invalid username"
            )

        if not user.verify_password(
            data["password"]
        ):
            raise ValueError(
                "Invalid password"
            )

        claims = {
            "role": user.role,
            "user_id": user.id
        }

        token = create_access_token(
            identity=str(user.username),
            additional_claims=claims
        )

        return token