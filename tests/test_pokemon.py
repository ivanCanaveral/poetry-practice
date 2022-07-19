""" dates.py tests """

import datetime
from unittest import TestCase
from unittest.mock import Mock
from src.pokemon import get_pikachu_id


class TestIsFriday(TestCase):
    """How to use Mock in tests"""

    def test_pikachu_id_wrong_version(self):
        """it gets the right id

        This tests does not work correctly.
        we override requests locally in this script,
        but it does not affect the behaviour
        of the function"""
        # Mock .today() to return Tuesday
        requests = Mock()
        requests.get.status_code = 200
        # we could change this value, and
        # tests will pass
        requests.get.return_value = {
            "name": "pikachu",
            "id": 25
        }
        self.assertEqual(get_pikachu_id(), 25)
