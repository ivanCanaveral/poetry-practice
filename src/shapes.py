""" some shape definitions """


class Rectangle:
    """it represents a rectangle"""

    def __init__(self, width: int, height: int) -> None:
        self.set_width(width)
        self.set_height(height)

    def get_area(self) -> None:
        """compute area"""
        return self.width * self.height

    def set_width(self, width: int) -> None:
        """sets width"""
        if width > 0:
            self.width = width
        else:
            raise TypeError

    def set_height(self, height: int) -> None:
        """sets height"""
        if height > 0:
            self.height = height
        else:
            raise TypeError
