from flask import Blueprint, request

import controllers

auth = Blueprint("auth", __name__)


@auth.route("/user/auth", methods=["POST"])
def auth_token_add():
    return controllers.auth_token_add(request)

# @auth.route("/user/logout", methods=["POST"])
# def logout(self):
#     return self.controller.logout()

# @auth.route("/user/check-login", methods=["GET"])
# def check_login_route():
#     return controllers.check_login()