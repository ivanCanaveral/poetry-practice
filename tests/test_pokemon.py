""" dates.py tests """

import datetime
from unittest import mock
import requests
from requests.exceptions import Timeout
from unittest import TestCase
from unittest.mock import Mock, patch
from src.pokemon import get_pikachu_order


class TestPikachuOrder(TestCase):
    """How to use Mock in tests

    After reading these examples you may be wondering
    where to patch a function. A good rule of thumb is
    to patch() the object where it is looked up.

    ! In the first example we are not patching ;)"""

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
        requests.get.json.return_value = {"name": "pikachu", "order": 24}
        self.assertEqual(get_pikachu_order(), 35)

    @patch("src.pokemon.requests")
    def test_pikachu_order_right_version(self, mocked_requests):
        """it gets the right order

        with a decorator, we patch the object
        for the whole function.

        In this case we don't need to import the target
        library (requests).
        """
        mocked_requests.get.status_code = 200
        # we could change this value, and
        # tests will pass
        mocked_requests.get.return_value.json.return_value = {
            "name": "pikachu",
            "id": 25,
            "order": 35,
        }
        self.assertEqual(get_pikachu_order(), 35)

    def test_pikachu_order_right_version_again(self):
        """it gets the right order

        we can also patch and object with a context
        manager to improve readability or to control
        the scope"""
        with patch("src.pokemon.requests") as mocked_requests:
            mocked_requests.get.status_code = 200
            # we could change this value, and
            # tests will pass
            mocked_requests.get.return_value.json.return_value = {
                "name": "pikachu",
                "id": 25,
                "order": 35,
            }
            self.assertEqual(get_pikachu_order(), 35)

    def test_pokemon_api_timeout(self):
        """it tests it raises a Timeout

        we can test more than one assert in a function"""
        with patch("src.pokemon.requests", autospec=True) as mocked_requests:
            mocked_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                _ = get_pikachu_order()
                # we can also test that we only call it once
                mocked_requests.get.assert_called_once()

    def test_pokemon_api_timeout_again(self):
        """it tests it raises a Timeout

        we can also patch concrete methods or
        attributes in an object. In this case
        we do really need to import the object.

        Unlike what happens in the first test,
        it works just patching the object/library
        globally.

        or even dicts, with patch.dict()

        We can also applay patch.object as a decorator:
        @patch.object(requests, 'get', side_effect=Timeout)
        """
        with patch.object(
            requests, "get", side_effect=Timeout
        ) as mocked_requests:
            with self.assertRaises(Timeout):
                _ = get_pikachu_order()

    def test_pokemon_api_timeout_again_again(self):
        """it tests it raises a Timeout

        Patching is very flexible, but you can easily
        write pointless test by mispelling or after
        changing a method or attribute name without
        updating your tests.

        To avoid that, you can use autospec. This option
        inspects the object, and limit the method or
        attribute names you can patch mock/patch.

        You can always define your specs manually.
        """
        with patch.object(
            requests, "get", side_effect=Timeout, autospec=True
        ) as mocked_requests:
            with self.assertRaises(Timeout):
                _ = get_pikachu_order()
