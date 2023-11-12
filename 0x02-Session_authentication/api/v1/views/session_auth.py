#!/usr/bin/env python3
"""Module for Session Authentication Views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Defines the login route for the user to login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return None

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            SESSION_NAME = getenv('SESSION_NAME')

            response = jsonify(user.to_json())
            response.set_cookie(SESSION_NAME, session_id)
            return response

    return jsonify({"error": "wrong password"}), 401


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def logout() -> str:
    """Defines the route to logout a user from the authentication system"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
