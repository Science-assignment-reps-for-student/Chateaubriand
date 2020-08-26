from test import BaseTestCase

from unittest.mock import patch

from chateaubriand.app.views.admin.experiment_assignment import ExperimentAssignmentView
from chateaubriand.app.exception import ViewError

class TestExperimentView(BaseTestCase):
    def setUp(self):
        self.experiment_assignment_view_post = ExperimentAssignmentView("1")

    @patch(
        'chateaubriand.app.views.admin.experiment_assignment.ExperimentAssignmentView.data_merge',
        return_value = (
            {
                "experiment_assignment":  [
                    {
                        "id": 1,
                        "title": "test",
                        "content": "test",
                        "created_at": 100000000,
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
        view = self.experiment_assignment_view_post.get_view()

        self.assertEqual(view, (
            {
                "experiment_assignment":  [
                    {
                        "id": 1,
                        "title": "test",
                        "content": "test",
                        "created_at": 100000000,
                        "deadline": 100000000,
                        "peer_evaluation_submit": [],
                        "teams_info": [],
                        "view": 0
                    }
                ]
            }, 200
        ))