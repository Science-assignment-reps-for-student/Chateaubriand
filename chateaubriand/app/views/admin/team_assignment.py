import time

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import HomeworkModel, StudentModel, TeamModel, MemberModel


class TeamAssignmentView(BaseView):
    def __init__(self, _class):
        self._class = _class

    def get_student_info(self, student_id):
        student_info = StudentModel.query.filter_by(id=student_id).first()
        return student_info.name, student_info.student_number

    def get_members(self, team):
        members = []
        for member in team.members:
            student_name, student_number = self.get_student_info(member.student_id)
            members.append({
                "name": student_name,
                "student": student_number
            })

        return members

    def get_teams_info(self, teams, homework_id):
        teams_info = []
        for team in teams:
            if team.homework_id == homework_id:
                members = self.get_members(team)
                teams_info.append({
                    "team_name": team.team,
                    "submit": "Submit",
                    "members": members
                })

        return teams_info


    def query_to_db(self):
        student_number_like = "_{}__".format(self._class)

        teams = TeamModel.query\
            .join(StudentModel)\
            .join(HomeworkModel)\
            .filter(StudentModel.student_number.like(student_number_like))\
            .filter(HomeworkModel.type == "MULTI")\
            .all()

        students = StudentModel.query.filter(StudentModel.student_number.like(student_number_like)).all()
        homeworks = HomeworkModel.query.filter(HomeworkModel.type == "MULTI").all()

        return teams, students, homeworks

    def data_merge(self):
        teams, students, homeworks = self.query_to_db()

        assignment = []

        for homework in homeworks:
            peer_evaluation_submit = []
            for student in students:
                peer_evaluation_submit.append({
                    "name": "오준상",
                    "student_number": "1101",
                    "submit": 0
                })

            teams_info = self.get_teams_info(teams, homework.id)

            assignment.append({
                "id": homework.id,
                "title": homework.title,
                "description": homework.description,
                "created_at": homework.created_at,
                "deadline": time.mktime(homework.created_at.timetuple()),
                "peer_evaluation_submit": peer_evaluation_submit,
                "teams_info": teams_info
            })

        return {"team_assignment": assignment}, 200

    def get_view(self):
        return self.data_merge()
