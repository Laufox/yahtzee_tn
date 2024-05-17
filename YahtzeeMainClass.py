from die import Die


class YahtzeeMainClass:

    # Initiates class by creating a list with five Die objects
    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die()]

    # Goes through all the die in dice and prints the face value if each die
    def show_dice_value(self):
        for i, die in enumerate(self.dice):
            print(f"{i}: Dice shows {die.get_die_value()}")

    # Returns true if all die in dice has same value as first die in dice list, otherwise returns false
    def check_if_yahtzee(self):
        return all(die.value == self.dice[0].value for die in self.dice)

    # Changes face value for each die
    def roll_dice(self):
        for die in self.dice:
            die.die_roll()

    # Gets face value for first die in dice list
    def get_first_die_value(self):
        return self.dice[0]