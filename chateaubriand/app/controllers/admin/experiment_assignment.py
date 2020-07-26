from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.experiment_assignment import ExperimentAssignmentView
from chateaubriand.app.util.token_checker import available_token
from chateaubriand.app.util.param_checker import param_validate, GET_ASSIGNMENT


class ExperimentAssignment(Resource):
    @param_validate(GET_ASSIGNMENT)
    @available_token
    def get(self):
        experiment_assignment_view = ExperimentAssignmentView(request.args.get("class"))
        view = experiment_assignment_view.get_view()
        return view
