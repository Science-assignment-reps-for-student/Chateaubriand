from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.team_assignment import TeamAssignmentView
from chateaubriand.app.util.json_checker import json_type_validate, GET_ASSIGNMENT_JSON
from chateaubriand.app.util.token_checker import available_token


class TeamAssignment(Resource):
    @json_type_validate(GET_ASSIGNMENT_JSON)
    @available_token
    def get(self):
        team_assignment_view = TeamAssignmentView(request.json["class"])
        view = team_assignment_view.get_view()
        return view