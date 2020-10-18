from test import BaseTestCase

from unittest.mock import patch

from chateaubriand.app.views.admin.assignment import AssignmentView

class TestAssignmentView(BaseTestCase):
    def setUp(self):
        self.assignment_view_post = AssignmentView("mock_id")

    @patch(
        'chateaubriand.app.views.admin.assignment.AssignmentView.data_merge',
        return_value = (
            {
                "id": "mock_id",
                "deadline_1": 1603020225,
                "deadline_2": 1603020225,
                "deadline_3": 1603020225,
                "deadline_4": 1603020225,
                "title": "test_title",
                "description": "test_description",
                "type": "PERSONAL",
                "created_at": 1603020225,
                "view": 1
            }, 200
        )
    )
    def test_post(self, mock_data):
        view = self.assignment_view_post.get_view()

        self.assertEqual(view, (
            {
                "id": "mock_id",
                "deadline_1": 1603020225,
                "deadline_2": 1603020225,
                "deadline_3": 1603020225,
                "deadline_4": 1603020225,
                "title": "test_title",
                "description": "test_description",
                "type": "PERSONAL",
                "created_at": 1603020225,
                "view": 1
            }, 200
        ))