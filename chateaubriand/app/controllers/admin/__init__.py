from flask import Blueprint
from flask_restful import Api

from chateaubriand.app.controllers.admin.personal_assignment import PersonalAssignment
from chateaubriand.app.controllers.admin.account import Account

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")
admin_api = Api(admin_blueprint)

admin_api.add_resource(PersonalAssignment, "/personal-assignment")
admin_api.add_resource(Account, "/account")
