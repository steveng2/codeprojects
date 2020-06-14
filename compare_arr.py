#a dice game that compare two dice if they have rolled the same number
#date: 14/06/2020
#Steven Garner

import random
import math


msg = "your turn"
score_target = 30
dice_one = random.randint(1,6)
dice_two = random.randint(1,6)
score = dice_one + dice_two
compare_dices = dice_one == dice_two
print(compare_dices)
print(dice_one)
print(dice_two)


def game():
    if compare_dices == dice_two and dice_one:
        print("The number was a doulbe")
    else:
        print("The number was not a double")
game()





