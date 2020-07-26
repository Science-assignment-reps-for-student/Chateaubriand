from flask import request
from flask_restful import Resource

from chateaubriand.app.services.admin.token import TokenService
from chateaubriand.app.views.admin.token import TokenView
from chateaubriand.app.util.json_checker import json_type_validate, POST_TOKEN_JSON


class Token(Resource):
    @json_type_validate(POST_TOKEN_JSON)
    def post(self):
        email = TokenService.check_token(
            request.json["access_token"], request.json["refresh_token"]
        )
        token_view = TokenView(email)
        view = token_view.get_view()
        return view
