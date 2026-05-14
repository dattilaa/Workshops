class Circle:
    """
    A class representing a circle.

    Class Attributes:
        pi (float): The mathematical constant pi, approximated as 3.1415.
        all_circles (list): A list containing all instances of the Circle class.

    Instance Attributes:
        radius (float): The radius of the circle. Defaults to 1.

    Methods:
        __init__(self, r=1): Initializes a new Circle instance with the given radius.
                              Automatically appends the instance to the all_circles list.

        __str__(self): Returns a string representation of the circle (its radius).

        area(self): Calculates and returns the area of the circle using the formula: pi * radius^2.

        total_area(): Static method that returns the total area of all Circle instances
                      created so far by summing the area of each circle in all_circles.
    """

    pi = 3.1415
    all_circles = []

    def __init__(self, r=1):
        """Initialize a new circle with the given radius."""
        self.radius = r
        Circle.all_circles.append(self)

    def __str__(self):
        """Return the radius of the circle as a string."""
        return f'{self.radius}'

    def area(self):
        """Calculate and return the area of the circle."""
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        """Return the total area of all created Circle instances."""
        return sum([circle.area() for circle in Circle.all_circles])








