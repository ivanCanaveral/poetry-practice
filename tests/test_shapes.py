import unittest

from src.shapes import Rectangle


class TestRectangle(unittest.TestCase):
    """tests Rectagle definition"""

    def test_area(self):
        """it computes area correctly"""
        my_rectangle: Rectangle = Rectangle(2, 2)
        self.assertEqual(my_rectangle.get_area(), 4)

    def test_negative_width(self):
        """it raises TypeError when width is non positive"""
        with self.assertRaises(TypeError):
            Rectangle(-1, 1)

    def test_negative_height(self):
        """it raises TypeError when height"""
        with self.assertRaises(TypeError):
            Rectangle(1, -1)
