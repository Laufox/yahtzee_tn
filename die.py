import random


class Die:

    # Initiates face value of die object to zero
    def __init__(self):
        self.value = 0
    
    # Returns face value of die object
    def get_die_value(self):
        return self.value

    # Changes face value of die to a random number
    def die_roll(self):
        self.value = random.randint(1,6)