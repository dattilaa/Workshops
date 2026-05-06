class TrafficLight:
    """
    A class representing a traffic light with a cycle of signals.

    Attributes:
        current_signal (str): The current traffic light signal ('Green', 'Yellow', 'Red').
        permissible_values (list): List of valid signal states in order.
    """

    def __init__(self):
        """Initialize a TrafficLight object with the starting signal 'Green'."""
        self.current_signal = 'Зеленый'
        self.permissible_values = ['Зеленый', 'Желтый', 'Красный']

    def next_signal(self):
        """
        Advance the traffic light to the next signal in the cycle.

        The cycle order is: Green -> Yellow -> Red -> Green.
        """
        ind = self.permissible_values.index(self.current_signal)
        if ind == len(self.permissible_values) - 1:
            ind = 0

        self.current_signal = self.permissible_values[ind + 1]


seven_roads = TrafficLight()
print(seven_roads.current_signal)
for _ in range(5):
    seven_roads.next_signal()
print(seven_roads.current_signal)