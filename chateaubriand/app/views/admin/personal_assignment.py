import time

from chateaubriand.app.exception import BadRequest
from chateaubriand.app.views import BaseView
from chateaubriand.app.models import(
 HomeworkModel, StudentModel, SingleFileModel
)

class PersonalAssignmentView(BaseView):
    def __init__(self, class_):
        self.class_ = class_

    def deadline(self, assignment):
        if self.class_ == 1:
            return assignment.deadline_1
        elif self.class_ == 2:
            return assignment.deadline_2
        elif self.class_ == 3:
            return assignment.deadline_3
        elif self.class_ == 4:
            return assignment.deadline_4
        else:
            raise BadRequest

    def query_to_db(self):
        student_number_like = "_{}__".format(self.class_)

        queried_data = HomeworkModel.query\
            .join(SingleFileModel)\
            .join(StudentModel)\
            .filter(StudentModel.student_number.like(student_number_like))\
            .filter(HomeworkModel.type == "SINGLE")\
            .all()

        return queried_data
        #
        # for i in queried_data:
        #     print(i, i.single_files, i.single_files[0].students)

    def data_merge(self):
        queried_data = self.query_to_db()
        assignments = []

        for assignment in queried_data:
            class_submit = []

            for single_file in assignment.single_files:
                class_submit.append(
                    {
                        "name": single_file.students.name,
                        "student_id": single_file.students.id,
                        "submit": 1
                    }
                )


            assignments.append(
                {
                    "id": assignment.id,
                    "title": assignment.title,
                    "description": assignment.description,
                    "created_at": time.mktime(assignment.created_at.timetuple()),
                    "deadline": time.mktime(self.deadline(assignment).timetuple()),
                    "class_submit": class_submit
                }
            )


        return {
            "personal_assignment":
        }


    def get_view(self):
        self.query_to_db()
        return None
        # return {
        #     "personal_assignment": [
        #         {
        #             "id": 1,
        #           "title": "정우영의 전구공장",
        #           "description": "description of homework",
        #           "created_at": time.mktime(personal_homework.created_at.timetuple()),
        #             "deadline": time.mktime(),
        #             "class_submit": [
        #                 {
        #                     "name": "오준상",
        #                     "student_id": "1101",
        #                     "submit": 0
        #                 },
        #                 {
        #                     "name": "김어진",
        #                     "student_id": "1102",
        #                     "submit": 1
        #                 }
        #             ]
        #         }
        #     ]
        # }