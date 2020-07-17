from flask import request
from flask_restful import Resource

from chateaubriand.app.services.admin.auth import AuthService
from chateaubriand.app.views.admin.account import AccountView
from chateaubriand.app.util.json_checker import json_type_validate, POST_AUTH_JSON

class Auth(Resource):
    @json_type_validate(POST_AUTH_JSON)
    def post(self):
        AuthService.login(request.json["email"], request.json["password"])
        auth_view = AccountView(request.json["email"])
        view = auth_view.get_view()
        return view
