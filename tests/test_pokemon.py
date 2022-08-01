""" dates.py tests """

import datetime
from unittest import mock
import requests
from requests.exceptions import Timeout
from unittest import TestCase
from unittest.mock import Mock, patch
from src.pokemon import get_pikachu_order


class TestPikachuOrder(TestCase):
    """How to use Mock in tests"""

    def test_pikachu_order_wrong_version(self):
        """it gets the right order

        This tests does not work correctly.
        we override requests locally in this script,
        but it does not affect the behaviour
        of the function"""
        # Mock() helps mocking objects
        requests = Mock()
        requests.get.status_code = 200
        # we could change this value, and
        # tests will pass
        requests.get.json.return_value = {
            "name": "pikachu",
            "order": 24
        }
        self.assertEqual(get_pikachu_order(), 35)

    @patch('src.pokemon.requests')
    def test_pikachu_order_right_version(self, mocked_requests):
        """it gets the right order

        with a decorator, we patch the object
        for the whole function.
        """
        mocked_requests.get.status_code = 200
        # we could change this value, and
        # tests will pass
        mocked_requests.get.return_value.json.return_value = {
            "name": "pikachu",
            "id": 25,
            "order": 35
        }
        self.assertEqual(get_pikachu_order(), 35)

    def test_pikachu_order_right_version_again(self):
        """it gets the right order

        we can also patch and object with a context
        manager to improve readability or to control
        the scope"""
        with patch('src.pokemon.requests') as mocked_requests:
            mocked_requests.get.status_code = 200
            # we could change this value, and
            # tests will pass
            mocked_requests.get.return_value.json.return_value = {
                "name": "pikachu",
                "id": 25,
                "order": 35
            }
            self.assertEqual(get_pikachu_order(), 35)

    def test_pokemon_api_timeout(self):
        """ it tests it raises a Timeout

        we can test more than one assert in a function"""
        with patch('src.pokemon.requests') as mocked_requests:
            mocked_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                _ = get_pikachu_order()
                # we can also test that we only call it once
                mocked_requests.get.assert_called_once()
