import random

worlds = [
    "apple",
    "bannana",
    "orange",
    "coconut",
    "lime",
    "lemon",
    "kumquat",
    "blueberry"

]

while True :
    start = input(" please enter start or enter Q to quit: ")

    if start.lower() == 'q':
        break

    secret_world = random.choice(worlds)

    good_guesses = []
    bad_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_world)):
        for letter in secret_world:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print('')
        print(f'strikes: {len(bad_guesses)}/7')
        print('')

        guess= input("Guess a letter:").lower()

        if len(guess) != 1 :
            print("You can only guess a single letter:")
            continue
        elif guess in bad_guesses or guess in good_guesses:
             print("You have already guess that letter")
             continue 
        elif  not guess.isalpha():
            print(" You can only guess letters")
        
        if guess in secret_world:
            good_guesses.append(guess)

            if len(good_guesses) == len(list(secret_world)):
                print("You Win!' The world was {}".format(secret_world))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("you didn't guess it! My secret world was{}".format(secret_world))


        

