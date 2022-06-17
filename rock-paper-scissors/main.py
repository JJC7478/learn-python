from random import *

MOVES = ["rock", "paper", "scissors"]

ai_move = choice(MOVES)

player_move = input("Rock, paper, or scissors?").lower()

if ai_move == player_move:
    print("draw")
elif player_move == "rock":
    if ai_move == "paper":
        print("ai wins")
    elif ai_move == "scissors":
        print("player wins")
elif player_move == "paper":
    if ai_move == "rock":
        print("player wins")
    elif ai_move == "scissors":
        print("ai wins")
elif player_move == "scissors":
    if ai_move == "rock":
        print("ai wins")
    elif ai_move == "paper":
        print("player wins")