import random
#Instructions for the player
#Rock beats scissors, scissors beat paper, and paper beats rock
print("")
print("*Rock-Paper-Scissors Game*")
print("<------------------------>")
print("\aRock beats scissors, scissors beat paper, and paper beats rock!\a")
print("Rock    -->'R'\nPaper   -->'P'\nScissor -->'S'")
print()
x=input("Press enter to start the game!")
while x=="":
    #Main progarm
    MOVES = "R", "P", "S"
    choice_By_Computer = random.choice(MOVES)
    move_by_player = input("Enter your move: ")
    move_by_player = move_by_player.upper()
    print()
    if move_by_player=="R" or move_by_player=="P" or move_by_player=="S":
        print("Computer's choice--->", choice_By_Computer)
        if move_by_player == choice_By_Computer:
            print("<---It's a tie--->")
        elif (move_by_player=='R' and choice_By_Computer=='S') or (move_by_player=='S' and choice_By_Computer=='P') or (move_by_player=='P' and choice_By_Computer=='R'):
            print("<---You Won--->")
        elif (move_by_player=='S' and choice_By_Computer=='R') or (move_by_player=='P' and choice_By_Computer=='S') or (move_by_player=='R' and choice_By_Computer=='P'):
            print("<---You lose--->")
    else:
        print("Enter choice from the given options i.e('R','P','S')")
        print()
    print("")
    x = input("Press enter to start the game!")

