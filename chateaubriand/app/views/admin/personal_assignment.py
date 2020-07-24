import time

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import AssignmentModel, StudentModel, PersonalFileModel


class PersonalAssignmentView(BaseView):
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

        exist_assignments = AssignmentModel.query\
            .join(PersonalFileModel)\
            .join(StudentModel)\
            .filter(StudentModel.student_number.like(student_number_like))\
            .filter(AssignmentModel.type == "SINGLE")\
            .all()

        students = StudentModel.query.filter(StudentModel.student_number.like(student_number_like)).all()
        assignments = AssignmentModel.query.filter(AssignmentModel.type == "SINGLE").all()

        return exist_assignments, students, assignments

    def data_merge(self):
        exist_assignments, students, assignments = self.query_to_db()
        assignments = []

        for assignment in assignments:
            class_submit = []

            for student in students:
                class_submit.append(
                    {
                        "name": student.name,
                        "student_number": student.student_number,
                        "submit": self.is_submit(assignment, student.student_number, exist_assignments)

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
