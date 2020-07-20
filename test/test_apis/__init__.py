from test.test_apis import (
    test_experiment_assignment_api,
    test_personal_assignment_api,
    test_team_assignment_api,
    test_account_api,
    test_auth_api,
    test_token_api
)

ExperimentAssignmentTestCase = test_experiment_assignment_api.ExperimentAssignmentTestCase
PersonalAssignmentTestCase = test_personal_assignment_api.PersonalAssignmentTestCase
TeamAssignmentTestCase = test_team_assignment_api.TeamAssignmentTestCase
AccountTestCase = test_account_api.AccountTestCase
AuthTestCase = test_auth_api.AuthTestCase
TokenTestCase = test_token_api.TokenTestCase