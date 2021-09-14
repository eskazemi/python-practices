import random
import os
# drow grid
# pick random location for the player
# pick random location for the exit door
# pick random location for the  monster 
# draw a player in grid
# take inpot or movement
# move player, unless invalid move (past edges of grid)
# clear screen and random grid


CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,0),(4,2),
    (0,3),(1,3),(2,3),(3,0),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4)
 ]



def clear_screen():
    os.system('cls' if os.name =='nt'  else 'Clear')




def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1

    return x, y

def get_move(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x ,y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0 :
        moves.remove("UP") 
    if y == 4:
        moves.remove("DOWN")

    return moves




def get_locations():
    return random.sample(CELLS, 3)


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("x|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)





def game_loop( ):
    monster , door , player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print(f"you are currently in room {player}") 
        print("you can move {}".format(' '.join(valid_moves)))
        print("Enter 'QUIT' to quite.")

        move = input("> ")
        move = move.upper()

        if move  == 'QUIT':
            break

        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                print("\n ** OH NO! The monster got you! luck next time! ** \n")
                playing = False
            elif player == door:
                print("\n ** You Scaped!  **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into tahn!**\n")
    else:
        if input("play again? [Y/N]").lower() != "n":
            game_loop()




clear_screen()
print("Welcom to teh dungeon!")
input(" press return to start!")
clear_screen()
game_loop()
    