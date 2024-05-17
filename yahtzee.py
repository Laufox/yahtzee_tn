from YahtzeeMainClass import YahtzeeMainClass


def main():
    # Initiate an object from YahtzeeMainClass class and assign it to variable game_dice
    game_dice = YahtzeeMainClass()
    
    print("Welcome to Yahtzee!")

    # Main game loop that loops until the player gets yahtzee or the player decides not to play anymore
    while True:
        turn = 1

        # Round loop that loops until three rounds has been play, the player gets yahtzee or the player decides not to throw again
        while turn <= 3:
            print(f"Starting turn: {turn} of 3, rolling dice")

            # Rolls all the dice and displays their value
            game_dice.roll_dice()
            game_dice.show_dice_value()

            # If player gets yahtzee, inform player and return from main function
            if game_dice.check_if_yahtzee():
                print(f"You got YAHTZEE! in {game_dice.get_first_die_value()}'s")
                return
            elif turn != 3:
                # Ask player for another round, and return from function if answer is anything other than "y"
                throw_again_input = input("Want to throw again? (y for yes, anything else for no) ")
                if throw_again_input != "y":
                    return
                
            turn += 1

        # Ask player for another game, and return from function if answer is anything other than "y"
        choice = input("Game over! Want to play again? ")
        if choice != "y":
            return


if __name__ == '__main__':
    main()