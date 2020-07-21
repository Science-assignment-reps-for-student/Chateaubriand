from flask import request
from flask_restful import Resource

from chateaubriand.app.services.admin.account import AccountService
from chateaubriand.app.views.admin.account import AccountView
from chateaubriand.app.util.json_checker import json_type_validate, POST_ACCOUNT_JSON, DELETE_ACCOUNT_JSON
from chateaubriand.app.util.token_checker import available_token

class Account(Resource):
    @json_type_validate(POST_ACCOUNT_JSON)
    def post(self):
        AccountService.create_account(request.json["email"], request.json["password"], request.json["name"])
        account_view = AccountView("POST")
        view = account_view.get_view()
        return view

    @json_type_validate(DELETE_ACCOUNT_JSON)
    @available_token
    def delete(self):
        AccountService.delete_account(request.json["email"], request.json["password"])
        account_view = AccountView("DELETE")
        view = account_view.get_view()
        return view



