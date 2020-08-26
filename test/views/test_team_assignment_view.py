from test import BaseTestCase

from unittest.mock import patch

from chateaubriand.app.views.admin.team_assignment import TeamAssignmentView
from chateaubriand.app.exception import ViewError

class TestTeamView(BaseTestCase):
    def setUp(self):
        self.team_assignment_view_post = TeamAssignmentView("1")

    @patch(
        'chateaubriand.app.views.admin.team_assignment.TeamAssignmentView.data_merge',
        return_value = (
            {
                "team_assignment": [
                    {
                        "id": 1,
                        "title": "test",
                        "content": "test",
                        "created_at": 10000000,
                        "deadline": 100000000,
                        "peer_evaluation_submit": [],
                        "teams_info": [],
                        "view": 0
                    }
                ]
            }, 200
        )
    )
    def test_post(self, mock_data):
        view = self.team_assignment_view_post.get_view()

        self.assertEqual(view, (
            {
                "team_assignment": [
                    {
                        "id": 1,
                        "title": "test",
                        "content": "test",
                        "created_at": 10000000,
                        "deadline": 100000000,
                        "peer_evaluation_submit": [],
                        "teams_info": [],
                        "view": 0
                    }
                ]
            }, 200
        ))