import random
secret_number = random.randint(1,20)



def run_game():
    gueses = []
    guest = 0
    while len(gueses) < 6:
        try:
            guest = int(input("guest a number between 1 to 20 :")) 
        except ValueError:
            print(f"{guest}is not a number")
        else:
            if guest == secret_number:
                print("you win!."+f"my number was {secret_number}")
                break
            elif guest < secret_number:
                print("My number is Bigger than guest")
            elif guest > secret_number:
                print("My  number is Smaller than guest")
            gueses.append(gueses)
    else:
        print(f"you didn't get it. My number {secret_number}")

    play_agein = input(" do you want to play again? [y/n]")
    if play_agein.lower() != 'n':
        run_game()
    else:
        print("Bye")
        

run_game()
      