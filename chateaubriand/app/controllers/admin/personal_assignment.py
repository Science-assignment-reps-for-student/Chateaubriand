from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.personal_assignment import PersonalAssignmentView
from chateaubriand.app.util.json_checker import json_type_validate, GET_ASSIGNMENT_JSON


class PersonalAssignment(Resource):
    @json_type_validate(GET_ASSIGNMENT_JSON)
    def get(self):
        personal_assignment_view = PersonalAssignmentView(request.json["class"])
        view = personal_assignment_view.get_view()
        return view
