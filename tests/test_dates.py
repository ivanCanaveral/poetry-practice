""" dates.py tests """

import datetime
from unittest import TestCase
from unittest.mock import Mock
from src.dates import is_friday


class TestIsFriday(TestCase):
    """How to use Mock in tests"""

    def __init__(self, *args, **kwargs):
        """this sets up all
        the commmon stuff in this test
        """
        super(TestIsFriday, self).__init__(*args, **kwargs)
        self.tuesday = datetime.datetime(year=2022, month=7, day=12)
        self.friday = datetime.datetime(year=2022, month=7, day=15)

    def test_is_friday(self):
        """it detects fridays correctly"""
        # Mock .today() to return Tuesday
        datetime = Mock()
        datetime.datetime.today.return_value = self.friday
        self.assertTrue(is_friday(datetime.datetime.today()))

    def test_is_not_friday(self):
        """it detects fridays correctly"""
        # Mock .today() to return Tuesday
        datetime = Mock()
        datetime.datetime.today.return_value = self.tuesday
        self.assertFalse(is_friday(datetime.datetime.today()))
