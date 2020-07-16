import unittest

from types import FunctionType

from test.test_config import AppConfigTestCase
from test.test_apis import (
    PersonalAssignmentTestCase,
    TeamAssignmentTestCase,
    ExperimentAssignmentTestCase,
)


def get_test_key(module):
    keys = []
    for key, value in module.__dict__.items():
        if "test" in key and isinstance(value, FunctionType):
            keys.append(key)
    return keys


def add_tests(test_suite, modules):
    for module in modules:
        for test_method in get_test_key(module):
            test_suite.addTest(module(test_method))


def create_test_suite(modules):
    test_suite = unittest.TestSuite()
    add_tests(test_suite, modules)
    return test_suite


if __name__ == "__main__":
    test_suite = create_test_suite(
        [
            AppConfigTestCase,
            PersonalAssignmentTestCase,
            TeamAssignmentTestCase,
            ExperimentAssignmentTestCase,
        ]
    )
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
