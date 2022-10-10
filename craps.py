import random as r

outcom = {7: "WON", 11: "WON", 2:"LOST", 3:"LOST", 12: "LOST"}

def roll_dice():
    """
    Roll the sum of two dice 
    """
    dice_1 = r.randint(1,6)
    dice_2 = r.randint(1,6)
    dice_sum = dice_1 + dice_2
    print("played rolled" + " " + str(dice_1) +" "+ str(dice_2) + " = " + str(dice_sum))
    return dice_sum

def main(dice_sum):
    """
    Determines whether the player is a winner or loser based on the sum of two dice
    """
    game_status = "CONTINUE"
    mypoint = 0

    for key , value in outcom.items():
        if (key == dice_sum):
            game_status = value
    mypoint = dice_sum
    while (game_status == "CONTINUE"):
        roll = roll_dice()
        if roll == mypoint:
            game_status = "WON"
            break
        elif roll == 7:
            game_status = "LOST"
            break

    if game_status == "WON":
        print ("player Is Wins")

    else:
        print("player Is Loses") 


sum_score = roll_dice()
main(sum_score)