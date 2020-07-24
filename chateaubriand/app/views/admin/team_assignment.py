import time

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import AssignmentModel, StudentModel, TeamModel, MemberModel


class TeamAssignmentView(BaseView):
    def __init__(self, _class):
        self._class = _class

    def get_teams_info(self, assignment):
        teams_info = []
        teams = TeamModel.query.filter(TeamModel.assignment_id == assignment.id)\
            .join(MemberModel) \
            .filter(
                StudentModel.query.filter_by(id=TeamModel.leader_id).first()
                .student_number[1] == self._class)\
            .all()

        for team in teams:
            members = []
            for member in team.members:
                member_info = StudentModel.query.filter_by(id=member.student_id).first()
                members.append({
                    "name": member_info.name,
                    "student_number": member_info.student_number
                })
            teams_info.append({
                "team_name": team.name,
                "submit": 1,
                "members": members
            })

        return teams_info

    def query_to_db(self):
        student_number_like = "_{}__".format(self._class)

        assignments = AssignmentModel.query.filter(AssignmentModel.type == "TEAM").all()

        return assignments

    def data_merge(self):
        assignments_model = self.query_to_db()
        assignments = list()

        for assignment in assignments_model:
            # peer_evaluation_submit = self.get_evaluation(students)
            teams_info = self.get_teams_info(assignment)
            assignments.append({
                "id": assignment.id,
                "title": assignment.title,
                "description": assignment.description,
                "created_at": time.mktime(assignment.created_at.timetuple()),
                "deadline": time.mktime(assignment.created_at.timetuple()),
                # "peer_evaluation_submit": peer_evaluation_submit,
                "teams_info": teams_info
            })


        return {"team_assignment": assignments}, 200

    def get_view(self):
        return self.data_merge()