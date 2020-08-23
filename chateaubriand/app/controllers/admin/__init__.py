from flask import Blueprint
from flask_restful import Api

from chateaubriand.app.controllers.admin.personal_assignment import PersonalAssignment
from chateaubriand.app.controllers.admin.team_assignment import TeamAssignment
from chateaubriand.app.controllers.admin.experiment_assignment import (
    ExperimentAssignment,
)
from chateaubriand.app.controllers.admin.account import Account
from chateaubriand.app.controllers.admin.auth import Auth
from chateaubriand.app.controllers.admin.token import Token

admin_blueprint = Blueprint("chateaubriand", __name__, url_prefix="/v2/chateaubriand")
admin_api = Api(admin_blueprint)

admin_api.add_resource(PersonalAssignment, "/personal-assignment")
admin_api.add_resource(TeamAssignment, "/team-assignment")
admin_api.add_resource(ExperimentAssignment, "/experiment-assignment")
admin_api.add_resource(Account, "/account")
admin_api.add_resource(Auth, "/auth")
admin_api.add_resource(Token, "/token")
