class NotSleeping:

    def __init__(self, name, counter=0):
        self.name = name
        self.count_sheep = counter

    def add_sheep(self):
        self.count_sheep += 1

    def lost(self):
        self.count_sheep = 0

    def get_count_sheep(self):
        return self.count_sheep



