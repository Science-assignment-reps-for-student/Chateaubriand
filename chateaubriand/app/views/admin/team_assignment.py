import time

from chateaubriand.app.extensions import db
from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import (
    AssignmentModel,
    StudentModel,
    TeamModel,
    MemberModel,
    TeamFileModel,
    SelfEvaluationModel,
    TeamEvaluationModel,
)


class TeamAssignmentView(BaseView):
    def __init__(self, _class):
        self._class = _class

    def deadline(self, assignment):
        if self._class == "1":
            return assignment.deadline_1
        elif self._class == "2":
            return assignment.deadline_2
        elif self._class == "3":
            return assignment.deadline_3
        elif self._class == "4":
            return assignment.deadline_4
        else:
            raise BadRequest

    def get_teams_info(self, assignment):
        teams_info = []
        teams = (
            TeamModel.query.filter(TeamModel.assignment_id == assignment.id)
            .join(MemberModel)
            .all()
        )

        for team in teams:
            if (
                str(
                    StudentModel.query.filter(StudentModel.id == team.leader_id)
                    .first()
                    .student_number
                )[1]
                == self._class
            ):
                members = []
                for member in team.members:
                    member_info = StudentModel.query.filter_by(
                        id=member.student_id
                    ).first()
                    members.append(
                        {
                            "name": member_info.name,
                            "student_number": member_info.student_number,
                        }
                    )
                teams_info.append(
                    {
                        "team_id": team.id,
                        "team_name": team.name,
                        "submit": self.get_team_submit(team),
                        "members": members,
                    }
                )

        return teams_info

    def get_team_submit(self, team):
        team_file = TeamFileModel.query.filter_by(team_id=team.id).first()
        if not team_file:
            return 0
        if team_file.is_late == False:
            return 1
        return 2

    def get_evaluation(self, students, assignment_id):
        evaluation_submit = []

        for student in students:
            evaluation_submit.append(
                {
                    "student_id": student.id,
                    "name": student.name,
                    "student_number": student.student_number,
                    "submit": self.get_evaluation_submit(student, assignment_id),
                }
            )

        return evaluation_submit

    def get_evaluation_submit(self, student, assignment_id):
        self_evaluation = SelfEvaluationModel.query.filter(
            db.and_(
                SelfEvaluationModel.assignment_id == assignment_id,
                SelfEvaluationModel.student_id == student.id,
            )
        ).first()

        if not self_evaluation:
            return 0

        team = (
            TeamModel.query.filter(TeamModel.assignment_id == assignment_id)
            .join(MemberModel)
            .filter(MemberModel.student_id == student.id)
            .first()
        )

        if not team:
            return 2

        if (
            len(team.members)
            == len(
                TeamEvaluationModel.query.filter(
                    db.and_(
                        TeamEvaluationModel.student_id == student.id,
                        TeamEvaluationModel.assignment_id == assignment_id,
                    )
                ).all()
            )
            + 1
        ):
            return 1

        return 0

    def query_to_db(self):
        student_number_like = "_{}__".format(self._class)
        assignments = AssignmentModel.query.filter(AssignmentModel.type == "TEAM").all()
        students = StudentModel.query.filter(
            StudentModel.student_number.like(student_number_like)
        ).all()

        return assignments, students

    def data_merge(self):
        assignments_model, students = self.query_to_db()
        assignments = list()

        for assignment in assignments_model:
            peer_evaluation_submit = self.get_evaluation(students, assignment.id)
            teams_info = self.get_teams_info(assignment)
            assignments.append(
                {
                    "id": assignment.id,
                    "title": assignment.title,
                    "description": assignment.description,
                    "created_at": time.mktime(assignment.created_at.timetuple()),
                    "deadline": time.mktime(self.deadline(assignment).timetuple()),
                    "peer_evaluation_submit": peer_evaluation_submit,
                    "teams_info": teams_info,
                    "view":assignment.view
                }
            )

        return {"team_assignment": assignments}, 200

    def get_view(self):
        return self.data_merge()
