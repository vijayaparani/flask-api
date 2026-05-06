def validate_register_data(data):

    if not data:
        raise ValueError("Request body is missing")

    if not data.get("username"):
        raise ValueError("Username required")

    if not data.get("password"):
        raise ValueError("Password required")

    if len(data["password"]) < 3:
        raise ValueError(
            "Password too short"
        )