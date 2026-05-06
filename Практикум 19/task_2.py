class NotSleeping:
    """
    A class representing a person who cannot sleep and counts sheep.

    Attributes:
        name (str): The name of the person.
        count_sheep (int): The number of counted sheep.
    """

    def __init__(self, name, counter=0):
        """
        Initialize a NotSleeping object.

        Args:
            name (str): The name of the person.
            counter (int, optional): Initial sheep count. Defaults to 0.
        """
        self.name = name
        self.count_sheep = counter

    def add_sheep(self):
        """Increment the sheep counter by 1."""
        self.count_sheep += 1

    def lost(self):
        """Reset the sheep counter to zero."""
        self.count_sheep = 0

    def get_count_sheep(self):
        """
        Get the current sheep count.

        Returns:
            int: The number of counted sheep.
        """
        return self.count_sheep











