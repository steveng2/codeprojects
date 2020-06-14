#App is this a coin that you flipped:
#I will uses function and while loop if statement
i = 1

while i < 6:

    def flick_coin():
        heads = " heads "
        tails = " Tails "
        if heads == heads or tails == tails:

            print("You flicked " + heads + tails + " You did fllick a coins ")
        else:
            print(" You didnt flick a coin ")

    if i == 3:
        break
    i += 1

    flick_coin()

