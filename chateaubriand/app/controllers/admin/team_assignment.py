from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.team_assignment import TeamAssignmentView
from chateaubriand.app.util.param_checker import param_validate, GET_ASSIGNMENT
from chateaubriand.app.util.token_checker import available_token


class TeamAssignment(Resource):
    @param_validate(GET_ASSIGNMENT)
    @available_token
    def get(self):
        team_assignment_view = TeamAssignmentView(request.args.get("class"))
        view = team_assignment_view.get_view()
        return view
