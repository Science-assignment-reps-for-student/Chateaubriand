import time

from chateaubriand.app.extensions import db

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import AssignmentModel, StudentModel, PersonalFileModel


class PersonalAssignmentView(BaseView):
    def __init__(self, _class):
        self._class = _class

    def is_submit(self, assignment_id, student_id):
        personal_file = PersonalFileModel.query.filter(
            db.end_(
                assignment_id == PersonalFileModel.assignment_id,
                student_id == PersonalFileModel.student_id,
            )
        )

        if personal_file is None:
            return 0
        if personal_file.is_late == True:
            return 2
        return 1

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

    def query_to_db(self):
        student_number_like = "_{}__".format(self._class)

        assignments = AssignmentModel.query.filter(
            AssignmentModel.type == "SINGLE"
        ).all()
        students = StudentModel.query.filter(
            StudentModel.student_number.like(student_number_like)
        ).all()

        return assignments, students

    def data_merge(self):
        assignments_model, students = self.query_to_db()
        assignments = list()

        for assignment in assignments_model:
            class_submit = []

            for student in students:
                class_submit.append(
                    {
                        "name": student.name,
                        "student_number": student.student_number,
                        "submit": self.is_submit(
                            assignment, student.student_number, exist_assignments
                        ),
                    }
                )

            assignments.append(
                {
                    "id": assignment.id,
                    "title": assignment.title,
                    "description": assignment.description,
                    "created_at": time.mktime(assignment.created_at.timetuple()),
                    "deadline": time.mktime(self.deadline(assignment).timetuple()),
                    "class_submit": class_submit,
                }
            )

        return {"personal_assignment": assignments}, 200

    def get_view(self):
        return self.data_merge()
