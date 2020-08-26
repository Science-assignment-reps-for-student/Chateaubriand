from test import BaseTestCase

from unittest.mock import patch

from chateaubriand.app.views.admin.personal_assignment import PersonalAssignmentView
from chateaubriand.app.exception import ViewError

class TestPersonalView(BaseTestCase):
    def setUp(self):
        self.personal_assignment_view_post = PersonalAssignmentView("1")

    @patch(
        'chateaubriand.app.views.admin.personal_assignment.PersonalAssignmentView.data_merge',
        return_value = (
            {
                "personal_assignment": [
                    {
                        "id": 1,
                        "title": "test",
                        "description": "test",
                        "created_at": 10000000,
                        "deadline": 10000000,
                        "class_submit": [],
                        "view": 0
                    }
                ]
            }, 200
        )
    )
    def test_post(self, mock_data):
        view = self.personal_assignment_view_post.get_view()

        self.assertEqual(view, (
            {
                "personal_assignment": [
                    {
                        "id": 1,
                        "title": "test",
                        "description": "test",
                        "created_at": 10000000,
                        "deadline": 10000000,
                        "class_submit": [],
                        "view": 0
                    }
                ]
            }, 200
        ))