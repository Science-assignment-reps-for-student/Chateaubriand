from flask import request
from flask_restful import Resource

from chateaubriand.app.services.admin.account import AccountService
from chateaubriand.app.views.admin.account import AccountView
from chateaubriand.app.util.json_checker import json_type_validate, POST_ACCOUNT_JSON, DELETE_ACCOUNT_JSON

class Account(Resource):
    @json_type_validate(POST_ACCOUNT_JSON)
    def post(self):
        AccountService.create_account(request.json["email"], request.json["password"], request.json["name"])
        account_view = AccountView("POST")
        view = account_view.get_view()
        return view
