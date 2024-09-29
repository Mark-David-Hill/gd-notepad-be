from flask import Blueprint, request

import controllers

auth = Blueprint("auth", __name__)


@auth.route("/user/auth", methods=["POST"])
def auth_token_add():
    return controllers.auth_token_add(request)

# def logout(self):
#     return self.controller.logout()

# def check_login(self):
#     return self.controller.check_login()