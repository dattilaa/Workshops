class Point:
    """
    A class representing a point in 2D coordinate space.

    Attributes:
        x (float): X-coordinate of the point.
        y (float): Y-coordinate of the point.
    """

    def __init__(self, coord=(0, 0)):
        """
        Initialize a Point object.

        Args:
            coord (tuple, optional): Tuple of (x, y) coordinates. Defaults to (0, 0).
        """
        self.x = coord[0]
        self.y = coord[1]

    def __str__(self):
        """
        Return a string representation of the point.

        Returns:
            str: String in format '(x, y)'.
        """
        return f'{self.x, self.y}'

    def get_x(self):
        """
        Get the X-coordinate.

        Returns:
            float: The X-coordinate value.
        """
        return self.x

    def get_y(self):
        """
        Get the Y-coordinate.

        Returns:
            float: The Y-coordinate value.
        """
        return self.y

    def distance(self, other):
        """
        Calculate the Euclidean distance to another point.

        Args:
            other (Point): Another Point object.

        Returns:
            float: Euclidean distance between this point and the other point.
        """
        change_x = (other.x - self.x) ** 2
        change_y = (other.y - self.y) ** 2
        return (change_x + change_y) ** 0.5

    def sum(self, other):
        """
        Calculate the vector sum of this point and another point.

        Args:
            other (Point): Another Point object.

        Returns:
            tuple: A tuple (x1 + x2, y1 + y2).
        """
        return self.x + other.x, self.y + other.y


p = Point((3,-7))
print(p)
a = Point()
print(a)
print(a.get_x())
print(p.get_y())
c = Point((-2, 4))
print(p.distance(c))
d = c.sum(p)
print(d)
