from random import random
from config_prs import (
    GAME_CHOICE, 
    RULES,
    scoreboard)
import random


def get_user_choice():
    """
    This function get and validate input player , recursively
    Args:
        Not Argumnet
    Raises:
        ...
    Returns:
        user_input(str)
    """
    user_input = input("Enter your choice please (r, p, s): ")
    if user_input not in GAME_CHOICE:
        print("oooh, wrong choice, try againe please...")
        return get_user_choice()
    else:
        return user_input


def get_system_choice():
    """
    This function get random choice from GAME_CHOICE
    Args:
        Not Argumnet
    Raises:
        ...
    Returns:
        system choice
    """
    return random.choice(GAME_CHOICE)


def find_winner(user_choice, system_choice):
    """
    This function recieve  user_choice and system_choice , sort them and 
    compare with game rules
    Args:
        user_choice(str)
        system_choice(str)
    Raises:
        TypeError
    Returns:
        winner
    """
    match = {user_choice, system_choice}

    if len(match) == 1:
        return None
    else:
        return RULES[tuple(sorted(match))]


def update_score_board(result, game):
    """
    This function update scoreboard after each hand of the game show live result
    untile now + last hand result
    Args:
        result(dict)
        game(int)
    Raises:
        TypeError
    Returns:
        resutl live result untile now + last hand result
    """
    if result["user"] == 3:
        scoreboard["user"] += 1
        msg = "You Win"
    elif result["system"] == 3:
        scoreboard["system"] += 1
        msg = "You Loss"
    scoreboard["game"] = game
    print("##"*20)
    print("##", f'user:{scoreboard["user"]}'.ljust(16),"##")
    print("##", f'system:{scoreboard["system"]}'.ljust(16),"##")
    print("##", f'{msg}'.ljust(16),"##")
    print("##", f'game:{scoreboard["game"]}'.ljust(16),"##")
    print("##"*20)




def play():
    game = 0
    result = {"user": 0, "system":0}
    while result["user"] < 3 and result["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        print("Your choice: ", user_choice)
        print("system choice:", system_choice)
        winner = find_winner(user_choice, system_choice)
        if winner == user_choice:
            result["user"] += 1
            print("result : you win")
        elif winner == system_choice:
            result["system"] += 1
            print("result: you loss")
        else:
             print("result : Draw")
        game += 1
    
    update_score_board(result, game)
    play_again = input("do you want to play again? (y/n) ")
    if play_again =='y':
        play()


if __name__ == "__main__":
    play()