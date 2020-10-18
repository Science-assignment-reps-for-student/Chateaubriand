from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.assignment import AssignmentView
from chateaubriand.app.util.token_checker import available_token
from chateaubriand.app.util.json_checker import GET_ASSIGNMENT_JSON, json_type_validate


class Assignment(Resource):
    @json_type_validate(GET_ASSIGNMENT_JSON)
    @available_token
    def post(self):
        assignment_view = AssignmentView(request.json["assignment_id"])
        return assignment_view.get_view()
