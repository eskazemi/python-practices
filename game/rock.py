#! /usr/bin/python3
import random

class RPS_Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def action(self):
        actions = ["rock", "paper", "scissors"]
        return random.choice(actions)

    def win(self):
        self.score += 1

class RPSLS_Player(RPS_Player):
    def action(self):
        actions = ["rock", "paper", "scissors", "lizard", "spock"]
        return random.choice(actions)



def check_score(first, second):
    if first == "rock":
        if second == "paper" or second == "spock":
            return "lose"
        elif second == "scissors" or second == "lizard":
            return "win"
    elif first == "paper":
        if second == "scissors" or second == "lizard":
            return "lose"
        elif second == "rock" or second == "spock":
            return "win"
    elif first == "scissors":
        if second == "rock" or second == "spock":
            return "lose"
        elif second == "paper" or second == "lizard":
            return "win"
    elif first == "lizard":
        if second == "rock" or second == "scissors":
            return "lose"
        elif second == "paper" or second == "spock":
            return "win"
    elif first == "spock":
        if second == "paper" or second == "lizard":
            return "lose"
        elif second == "rock" or second == "scissors":
            return "win"
    else:
        return "draw"


def rps_game(first, second):
    action1, action2 = first.action(), second.action()
    #print("first: {}\tsecond: {}".format(action1, action2))
    result = check_score(action1, action2)
    if result == "win":
        first.win()
        #print("first won.")
    elif result == "lose":
        second.win()
        #print("second won.")

def match(first, second):
    while first.score < 100 and second.score < 100:
        rps_game(first, second)
    if first.score == 100:
        print("{} won 100 by {}".format(first.name, second.score))
    else:
        print("{} won 100 by {}".format(second.name, first.score))

def main():
    first = RPS_Player("Hasan")
    second = RPS_Player("Nima")
    match(first, second)

    third = RPSLS_Player("Mina")
    forth = RPSLS_Player("Akbar")
    match(third, forth)

if __name__ == "__main__":
    main()
