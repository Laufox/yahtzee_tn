from yahtzee import YahtzeeMainClass

import pytest


def test_is_yahtzee_when_all_dice_matches():
    test_dice = YahtzeeMainClass()
    
    for die in test_dice.dice:
        die.value = 6
    
    assert test_dice.check_if_yahtzee() == True


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    test_dice = YahtzeeMainClass()
    
    for die in test_dice.dice:
        die.value = 6
        
    test_dice.dice[0].value = 2
    
    assert test_dice.check_if_yahtzee() == False


if __name__ == '__main__':
    pytest.main()
