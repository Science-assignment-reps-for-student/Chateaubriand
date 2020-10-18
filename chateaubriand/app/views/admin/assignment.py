import time

from chateaubriand.app.views import BaseView
from chateaubriand.app.models import AssignmentModel


class AssignmentView(BaseView):
    def __init__(self, assignment_id):
        self._assignment_id = assignment_id

    def get_assignment(self):
        return AssignmentModel.query.filter(
            AssignmentModel.id == self._assignment_id
        ).first()

    def data_merge(self):
        assignment = self.get_assignment()
        return {
            "id": assignment.id,
            "deadline_1": time.mktime(assignment.deadline_1.timetuple()),
            "deadline_2": time.mktime(assignment.deadline_2.timetuple()),
            "deadline_3": time.mktime(assignment.deadline_3.timetuple()),
            "deadline_4": time.mktime(assignment.deadline_4.timetuple()),
            "title": assignment.title,
            "description": assignment.description,
            "type": assignment.type,
            "created_at": time.mktime(assignment.created_at.timetuple()),
            "view": assignment.view
        }, 200

    def get_view(self):
        return self.data_merge()
