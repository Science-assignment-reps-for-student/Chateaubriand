import time

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import HomeworkModel, StudentModel, SingleFileModel


class TeamAssignmentView(BaseView):
    def __init__(self, _class):
        self._class = _class

    def is_submit(self, assignment, student_number, exist_assignments):
        for exist_assignment in exist_assignments:
            if exist_assignment.id == assignment.id:
                for single_file in exist_assignment.single_files:
                    if single_file.student.student_number == student_number:
                        if single_file.is_late == 1: return 2
                        else: return 1
        return 0

    def deadline(self, assignment):
        if self._class == 1:
            return assignment.deadline_1
        elif self._class == 2:
            return assignment.deadline_2
        elif self._class == 3:
            return assignment.deadline_3
        elif self._class == 4:
            return assignment.deadline_4
        else:
            raise BadRequest

    def query_to_db(self):
        student_number_like = "_{}__".format(self._class)

        exist_assignments = HomeworkModel.query\
            .join(SingleFileModel)\
            .join(StudentModel)\
            .filter(StudentModel.student_number.like(student_number_like))\
            .filter(HomeworkModel.type == "SINGLE")\
            .all()

        students = StudentModel.query.filter(StudentModel.student_number.like(student_number_like)).all()
        homeworks = HomeworkModel.query.filter(HomeworkModel.type == "SINGLE").all()

        return exist_assignments, students, homeworks

    def data_merge(self):
        assignment = []
        assignment.append({
            "id": "id",
            "title": "title",
            "description": "description",
            "created_at": "created_at",
            "deadline": "deadline",
            "peer_evaluation_submit": [
				{
					"name": "오준상",
					"student_number": "1101",
					"submit": 0
				},
				{
					"name": "김어진",
					"student_number": "1102",
					"submit": 1
				}
			],
            "team_submit": [
				{
					"team_name": "앙김어眞",
					"submit": 0,
					"member": [
						{
							"name": "오준상",
							"student_number": "1101"
						},
						{
							"name": "김어진",
							"student_number": "1102"
						}
					]
				}
        })

        return {"team_assignment": assignment}, 200

    def get_view(self):
        return self.data_merge()
